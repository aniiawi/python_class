from __future__ import annotations

import re


# https://refactoring.guru/ru/design-patterns/chain-of-responsibility
class ValidatorRule:
    def __init__(self):
        self.rule = None
        self.predicate = ""
        self.next = None


class Validator:
    def __init__(self, validator_rules):
        self._begin = validator_rules

    def validate(self, data: str):
        ptr = self._begin
        while ptr is not None:
            fnd = re.match(ptr.rule, data)
            if fnd is not None and fnd.group(1) != ptr.predicate:
                raise Exception("Validation error")
            ptr = ptr.next


class ValidatorBuilder:
    def __init__(self):
        self._val = None
        self._ptr = None

    def add_rule(self, rule, predicate):
        validator_rule = ValidatorRule()
        validator_rule.rule = rule
        validator_rule.predicate = predicate
        if self._val is None:
            self._val = validator_rule
        else:
            self._ptr.next = validator_rule

        self._ptr = validator_rule
        return self

    def build(self):
        return Validator(self._val)


if __name__ == '__main__':
    validator = ValidatorBuilder().add_rule(r'^(.+)-', 'model').add_rule(r'.+-(.+)$', 'A132').build()
    validator.validate('model-A132')
    print('Validated')
    try:
        validator.validate('no-A132')
    except Exception as e:
        print("Got exception as expected", e)
