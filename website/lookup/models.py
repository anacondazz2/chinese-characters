from django.db import models

class Word(models.Model):
    traditional = models.CharField(max_length=50)
    simplified = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    english = models.CharField(max_length=200)


# Example from Django documentation:

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# Inside the models module contains classes Model, CharField, and DateTimeField.
# Each field is an instance of a Field class, e.g., CharField for character fields and DateTimeField for datetimes.
# Here Question inherits from models.Model, which means that it is a Django model, and Django will create a database table for it.
# Each field is represented by an instance of a Field class, e.g., CharField for character fields and DateTimeField for datetimes.
# The field's class attributes define the database column type, e.g., CharField is a VARCHAR in SQL.
# The field's class attributes can also define constraints, e.g., max_length=200.
# "date published" is a human-readable name for the field while pub_date is the machine-readable name.

# Foreign key relationships are defined using ForeignKey. This tells Django that each Choice is related to a single Question.
# The on_delete argument specifies the behavior to adopt when the referenced object is deleted.
# CASCADE means that when the referenced Question is deleted, also delete all related Choices.
# The ForeignKey field type is used to define many-to-one relationships.
# An example of a many-to-one relationship is the relationship between a Choice and a Question. The many side of the relationship is the Choice model, and the one side is the Question model.
