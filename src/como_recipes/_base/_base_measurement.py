import typing

import pydantic

from ._base_ingredient import Ingredient


class Measurement(pydantic.BaseModel):
    """
    A measurement is a specified amount of an ingredient.

    Parameters
    ----------
    amount : int | float | typing.Literal["enough"]
        Amount of the ingredient.
    unit : typing.Literal["portions", "grams"]
        Unit of the ingredient amount.
    ingredient : Ingredient
        Ingredient being measured.
    prefix : str, optional
        Prefix to be added to the rendered text of the ingredient in a recipe.
        For example, "minced" for the ingredient "garlic".
    suffix : str, optional
        Suffix to be added to the rendered text of the ingredient in a recipe.
        For example, ", room-temperature" for the ingredient "butter".

    """

    amount: float | int
    unit: typing.Literal["portions", "grams"]
    prefix: str | None = None
    ingredient: Ingredient
    suffix: str | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        representation = f'Measurement(amount={self.amount}, unit="{self.unit}"'

        if self.prefix is not None:
            representation += f", prefix={self.prefix})"

        representation += f", ingredient={self.ingredient!r}"

        if self.suffix is not None:
            representation += f", suffix={self.suffix})"

        representation += ")"

        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        return repr(self)

    def __eq__(self, other: "Measurement") -> bool:
        """
        Logic defining the `==` operator.

        Primarily used by consistency assertions in the tests.

        Compares only the contained fields of the object, not including its memory address (two imported instances
        of the class with the same fields will be considered equal).
        """
        fields_to_compare = ["amount", "unit", "ingredient"]
        result = all(getattr(self, field) == getattr(other, field) for field in fields_to_compare)

        return result

    __hash__ = None
