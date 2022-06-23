# TGramBot - Partially Auto-generated Telegram Bot Api Library Python
# Copyright (C) 2022  Anand <anandpskerala@gmail.com>

# TGramBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# TGramBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import re
import shutil
import json
from pathlib import Path

API_PATH = Path("compiler/api")
TYPES_DESTINATION_PATH = Path("tgrambot/types")
TEMPLATES_DESTINATION = Path('compiler/templates')

TG_CORE_TYPES = {
    "String": 'str',
    "Boolean": 'bool',
    "Integer": 'int',
    "Float": 'int'
}

BASE_TYPES = ['str', 'bool', 'int', 'None']

INPUT_TYPES = ["ForceReply", "ReplyKeyboardMarkup", "KeyboardButton",
               "KeyboardButtonPollType", "ReplyKeyboardRemove", "InlineKeyboardMarkup",
               "InlineKeyboardButton", "LoginUrl"]


WARNING = """
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#       This is an auto-generated file!       #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #
""".strip()

COPYRIGHT = """
# TGramBot - Partially Auto-generated Telegram Bot Api Library Python
# Copyright (C) 2022  Anand <anandpskerala@gmail.com>

# TGramBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# TGramBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
""".strip()


def snake(s: str):
    # https://stackoverflow.com/q/1175208
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def camel(s: str):
    return "".join([i[0].upper() + i[1:] for i in s.split("_")])


def build_types():
    shutil.rmtree(TYPES_DESTINATION_PATH, ignore_errors=True)
    os.makedirs(TYPES_DESTINATION_PATH, exist_ok=True)

    # Constructing Base TelegramObject
    with open(TEMPLATES_DESTINATION / "base.tmpl", mode='r') as basefile:
        base_tmpl = basefile.read()
        with open(TYPES_DESTINATION_PATH / "base.py", "w+") as base:
            base.write(base_tmpl.format(warning=WARNING, copyright=COPYRIGHT))

    # Read JSON file that contains api methods and types
    with open(API_PATH / 'api.json') as f:
        schema = json.loads(f.read()).get('types')
        # Main Template
        content_temp = open(TEMPLATES_DESTINATION / 'type_class.tmpl', mode='r').read()
        content = ''
        # Pending queue to avoid ForwardRefs and ConfigErrors in pydantic
        pending_objects = []
        not_pending = []

        # To Find subclasses of an object
        subclass_dict = {}
        chat_object = ''
        callbackquery_object = ''

        # Classes to be imported in __init__ file
        init_types = []
        for name, item in schema.items():
            init_types.append(name)
            comments = '\n    '.join(item.get('description'))
            fields = item.get('fields')
            subclasses = item.get('subtypes')
            super_class = ""
            if subclasses and len(subclasses) != 0:
                for subclass in subclasses:
                    subclass_dict.update({snake(subclass): snake(name)})

            class_object = camel(subclass_dict.get(snake(name))) if subclass_dict.get(snake(name)) is not None else 'TelegramObject'
            if fields is None:
                content += content_temp.format(
                    class_name=name,
                    class_object=class_object,
                    comments=comments,
                    fields="\n    pass",
                    super_class=super_class
                )
            else:
                field_text = ''
                super_class_props = []
                super_class_text = ''
                field_count = 0
                pending_objects_count = 0
                for field in fields:
                    typed_list = []
                    # Separate types of props and classify them
                    for types in field.get('types'):
                        def_types = TG_CORE_TYPES.get(types) if TG_CORE_TYPES.get(types) is not None else types
                        if def_types.startswith("Array of Array"):
                            import_type = TG_CORE_TYPES.get(def_types[18:]) if TG_CORE_TYPES.get(def_types[18:]) is not None else def_types[18:]
                            def_types = f"List[List[{TG_CORE_TYPES.get(f'{def_types[18:]}')}]]" if TG_CORE_TYPES.get(
                                f'{def_types[18:]}') is not None else f'List[List["{def_types[18:]}"]]'
                        elif def_types.startswith("Array of"):
                            import_type = TG_CORE_TYPES.get(def_types[9:]) if TG_CORE_TYPES.get(def_types[9:]) is not None else def_types[9:]
                            def_types = f"List[{TG_CORE_TYPES.get(f'{def_types[9:]}')}]" if TG_CORE_TYPES.get(
                                f'{def_types[9:]}') is not None else f'List["{def_types[9:]}"]'
                        else:
                            import_type = def_types
                            def_types = def_types if def_types in BASE_TYPES else f'"{def_types}"'
                        if import_type not in BASE_TYPES and import_type not in not_pending and import_type not in init_types:
                            pending_objects_count += 1
                        else:
                            not_pending.append(name)

                        typed_list.append(def_types)

                    typed = str(typed_list).replace("'", "")
                    cust_typed = f'Union{typed}' if len(typed_list) > 1 else typed[1:-1]
                    cust_field = cust_typed
                    field_name = field.get('name')
                    required = field.get('required')
                    extras = 'Field(default=None)'

                    if field_name == "from":
                        extras = 'Field(alias="from", default=None)'
                        field_name = "from_user"
                    if field_name is None:
                        continue
                    else:
                        field_text += f"\n    {field_name}: {cust_field} = {extras}"
                        field_count += 1

                    # Escape Objects with no props
                    if field_count == 0:
                        field_text += "\n    pass"

                    if name in INPUT_TYPES:
                        if required:
                            super_class_props.append(f'{field_name}: {cust_field}')
                        else:
                            if field_name == 'url':
                                super_class_props.append(f'{field_name}: {cust_field} = ""')
                            else:
                                super_class_props.append(f'{field_name}: {cust_field} = None')

                        super_class_text += f'{field_name}={field_name}, '

                if len(super_class_props) > 0 and super_class_text != "":
                    super_class += f"""\n    def __init__(self, {', '.join(super_class_props)}):\n        super({name}, self).__init__({super_class_text[:-2]})\n"""

                # To avoid ForwardRefs and ConfigErrors in pydantic
                if name == "Chat":
                    chat_object += content_temp.format(
                        class_name=name,
                        class_object=class_object,
                        comments=comments,
                        fields=field_text,
                        super_class=super_class
                    )
                    continue

                if name == "CallbackQuery":
                    callbackquery_object += content_temp.format(
                        class_name=name,
                        class_object=class_object,
                        comments=comments,
                        fields=field_text,
                        super_class=super_class
                    )
                    continue

                if pending_objects_count > 0:
                    pending_objects.append(content_temp.format(
                        class_name=name,
                        class_object=class_object,
                        comments=comments,
                        fields=field_text,
                        super_class=super_class
                    ))
                else:
                    content += content_temp.format(
                        class_name=name,
                        class_object=class_object,
                        comments=comments,
                        fields=field_text,
                        super_class=super_class
                    )

        # To avoid ForwardRefs and ConfigErrors in pydantic
        for pending in reversed(pending_objects):
            if pending.startswith('class Message('):
                content += chat_object
                content += pending
                content += callbackquery_object
            else:
                content += pending

        # Constructing python module with all Telegram Objects
        with open(TYPES_DESTINATION_PATH / "tg_types.py", "w+") as type_file:
            with open(TEMPLATES_DESTINATION / 'types.tmpl', 'r') as type_temp_file:
                type_temp = type_temp_file.read()
                type_file.write(type_temp.format(
                    copyright=COPYRIGHT,
                    warning=WARNING,
                    content=content
                ))

        # Constructing __init__.py for types
        with open(TYPES_DESTINATION_PATH / '__init__.py', "w+") as type_init_file:
            with open(TEMPLATES_DESTINATION / 'init.tmpl', 'r') as type_init_temp_file:
                type_init_temp = type_init_temp_file.read()
                init_imports = ",\n    ".join(init_types)
                # Beautifying the imports
                list_imports = [init_types[i:i+4] for i in range(0, len(init_types), 4)]
                types_to_import = ""
                for lt in list_imports:
                    types_to_import += str(lt).replace("[", "").replace("]", "") + ",\n    "
                type_init_file.write(type_init_temp.format(
                    copyright=COPYRIGHT,
                    warning=WARNING,
                    imports=init_imports,
                    all=types_to_import[:-6]
                ))
