import yaml
import yamale   
from yamale.validators import DefaultValidators, Validator

class NullableStr(Validator):
   tag = 'nullable_str'
  
   def _is_valid(self, value):
      # Allow the value if it's explicitly None, or if it's a valid string instance
      return value is None or isinstance(value, str)

validators = DefaultValidators.copy()
validators[NullableStr.tag] = NullableStr

schema = yamale.make_schema('./layers_schema.yaml', validators=validators)

data = yamale.make_data('./layers.yaml')

results = yamale.validate(schema, data)

for result in results:
   if result.isValid():
      print(f"Success! {result.data} is perfectly valid against {result.schema}.")
   else:
      print(f"Validation failed for {result.data}:")
      print(result.errors)

