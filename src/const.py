class _ConstBase:
    """
    Proceed Constants
        - get_name: get the name of constant by type_, replaced "_" as " " and format by str().title()
        - get_type: format name by str().upper() and replaced " " as "_" to get the type of constant.

    e.g.
        class CONTINENT(_ConstBase):
            AFRICA = 1
            ASIA = 2
            EUROPE = 3
            NORTH_AMERICA = 4
            OCEANIA = 5
            SOUTH_AMERICA = 6

        continent = CONTINENT.get_name(CONTINENT.NORTH_AMERICA)
        print(continent)  ## North America

        continent_id = CONTINENT.get_type('nOrTh AMERICA')
        print(continent_id)  ## 4
    """

    _INVALID_TYPE = {classmethod, staticmethod}
    _STR_FORMAT_TYPE = {'title', 'upper', 'lower'}

    @classmethod
    def get_name(cls, type_, format_=None, blank_replacement=None):
        blank_replacement = blank_replacement or ' '
        if not isinstance(blank_replacement, str):
            raise ValueError(f'Invalid replacement {blank_replacement}')
        format_ = format_ or 'title'
        if format_.lower() not in cls._STR_FORMAT_TYPE:
            raise ValueError(f'Invalid format type {format_}')
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            if v == type_:
                return getattr(k.replace('_', blank_replacement), format_.lower())()

    @classmethod
    def get_type(cls, name):
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            if isinstance(name, str) and k == name.replace(' ', '_').upper():
                return v

    @classmethod
    def validate_type(cls, type_):
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            if v == type_:
                return True
        raise ValueError(f'Invalid type of {cls.__name__}: {type_}')

    @classmethod
    def validate_name(cls, name):
        if not isinstance(name, str):
            raise TypeError(f'name must be str, not {type(name)}')
        if name.replace(' ', '_').upper() not in cls.__dict__:
            raise ValueError(f'Invalid type of {cls.__name__}: {name}')
        return True

    @classmethod
    def get_elements(cls):
        elements = set()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            elements.add(v)
        return elements


class Const(_ConstBase):

    class Page(_ConstBase):
        PAGE = 5
        PER_PAGE = 5

    class Grade(_ConstBase):
        GRADE1 = 1
        GRADE2 = 2
        GRADE3 = 3


if __name__ == '__main__':
    print(Const.Grade.get_elements())


