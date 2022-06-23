import re
import json
from pathlib import Path

API_PATH = Path("compiler/api")
METHODS_DESTINATION_PATH = Path("tgrambot")
TEMPLATES_DESTINATION = Path('compiler/templates')

TG_CORE_TYPES = {
    "String": 'str',
    "Boolean": 'bool',
    "Integer": 'int',
    "Float": 'int'
}

BASE_TYPES = ['str', 'bool', 'int', 'None']

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


def build_methods():

    with open(API_PATH / 'api.json') as f:
        schema = json.loads(f.read()).get('methods')
        content = ''
        to_import = []
        # Main Template
        content_temp = open(TEMPLATES_DESTINATION / 'methods.tmpl', mode='r').read()
        for name, item in schema.items():
            field_text = "self, "
            required = ''
            non_required = ''
            returns_list = item.get('returns')
            attach_file = []
            comments = '\n        '.join(item.get('description')) + f"\n\n        Source : {item.get('href')}"
            fields = item.get('fields')
            method = snake(name)
            if fields:
                returns = ''
                for field in fields:
                    typed_list = []
                    field_name = field.get('name')
                    for types in field.get('types'):
                        def_types = TG_CORE_TYPES.get(types) if TG_CORE_TYPES.get(types) is not None else types
                        if def_types.startswith("Array of Array"):
                            import_type = TG_CORE_TYPES.get(def_types[18:]) if TG_CORE_TYPES.get(def_types[18:]) is not None else def_types[18:]
                            def_types = f"List[List[{TG_CORE_TYPES.get(f'{def_types[18:]}')}]]" if TG_CORE_TYPES.get(
                                f'{def_types[18:]}') is not None else f'List[List[{def_types[18:]}]]'
                        elif def_types.startswith("Array of"):
                            import_type = TG_CORE_TYPES.get(def_types[9:]) if TG_CORE_TYPES.get(def_types[9:]) is not None else def_types[9:]
                            def_types = f"List[{TG_CORE_TYPES.get(f'{def_types[9:]}')}]" if TG_CORE_TYPES.get(
                                f'{def_types[9:]}') is not None else f'List[{def_types[9:]}]'
                        else:
                            import_type = def_types
                            def_types = def_types if def_types in BASE_TYPES else f'{def_types}'

                        if import_type not in to_import and import_type not in BASE_TYPES:
                            to_import.append(import_type)

                        if import_type == "InputFile":
                            attach_file.append(field_name)
                        typed_list.append(def_types)

                    typed = str(typed_list).replace("'", "")
                    cust_typed = f'Union{typed}' if len(typed_list) > 1 else typed[1:-1]
                    if field_name:
                        if field.get('required'):
                            required += f"{field_name}: {cust_typed}, "
                        else:
                            non_required += f"{field_name}: {cust_typed} = None, "

                raw_return = TG_CORE_TYPES.get(returns_list[0]) if TG_CORE_TYPES.get(returns_list[0]) is not None else returns_list[0]
                if raw_return.startswith("Array of"):
                    raw_return = TG_CORE_TYPES.get(raw_return[9:]) if TG_CORE_TYPES.get(raw_return[9:]) is not None else raw_return[9:]
                    returns = f'[{raw_return}(**r) for r in result]'
                else:
                    if raw_return in BASE_TYPES:
                        returns = f'result'
                    else:
                        returns = f'{raw_return}(**result)'

                if raw_return not in to_import and raw_return not in BASE_TYPES:
                    to_import.append(raw_return)

                attach_content = ''
                if len(attach_file) > 0:
                    for attachs in attach_file:
                        attach_content += f"\n        if self._bot.attach_file(payload, '{attachs}', {attachs}) is not None:\n            files.update(self._bot.attach_file(payload, '{attachs}', {attachs}))"
                field_text += required + non_required
                content += content_temp.format(
                    name=name,
                    method_name=method,
                    fields=field_text[:-2],
                    attachment=attach_content,
                    comments=comments,
                    returns=returns
                )

        with open(METHODS_DESTINATION_PATH / 'methods.py', mode="w+") as file:
            main_temp = open(TEMPLATES_DESTINATION / 'method_class.tmpl', mode='r').read()
            file.write(main_temp.format(
                content=content,
                imports=",\n    ".join(to_import),
                copyright=COPYRIGHT,
                warning=WARNING
            ))
