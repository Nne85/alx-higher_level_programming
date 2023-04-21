#!/usr/bin/python3
"""
Base Module
"""
import json
import csv
import turtle


class Base:
    """
    The Base Class
    Attributes:
        __nb_object : private class atribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init
        Attributes:
            id (): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return A JSON STRING a representation list_dict..
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save Dict To Json
        """
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """
            Write Json Representation of String
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with
            all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            a = cls(1, 1)
        if cls.__name__ == 'Square':
            a = cls(1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """
            Load List of Instance from JSON File
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        ld = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        ld.append([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == 'Square':
                        ld.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(f)
            for row in ld:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                ld = []
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                ld.append(row)
                return [cls.create(**item) for item in ld]
        except FileNotFoundError:
            return []

        @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw the rectangle and the square using turtle module

        Args:
            list_rectangle: List of rectangle objects
            list_squares: List of square objects
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b6578f")
        tur.pensize(2)
        tur.shape("square")

        tur.color("#ffffff")
        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()
            for i in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()
            tur.color("#e8543f")

        for sqr in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sqr.x, sqr.y)
            tur.down()
            for i in range(2):
                tur.forward(sqr.width)
                tur.left(90)
                tur.forward(sqr.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
