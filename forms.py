from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# jst: Emailvalidation uitzoeken

"""
class wtforms.fields.RadioField(default field arguments, choices=[], coerce=str)[source]

    Like a SelectField, except displays a list of radio buttons.

    Iterating the field will produce subfields (each containing a label as well) in order to allow custom rendering of the individual radio fields.

    {% for subfield in form.radio %}
        <tr>
            <td>{{ subfield }}</td>
            <td>{{ subfield.label }}</td>
        </tr>
    {% endfor %}

    Simply outputting the field without iterating its subfields will result in a <ul> list of radio choices.
    
    Example: https://stackoverflow.com/questions/40986924/render-flask-wtforms-radiofield-lines-buttons-in-an-ordered-list
"""


class Vraag:    v_clusterNr = None
    v_number = None
    v_number_in_cluster = None
    v_text = None

    veld = RadioField(v_text, choices=['Geheel niet','Niet zo', 'Gemiddeld', 'Matig', 'Sterk of Ja!'])

    def __init__(self, v_clusterNr, v_number, v_number_in_cluster, v_text):
         self.v_clusterNr = v_clusterNr
         self.v_number = v_number
         self.v_number_in_cluster = v_number_in_cluster
         self.v_text = v_text



class VragenlijstForm(FlaskForm):
    user_first_name = StringField('Voornaam',
                           validators=[DataRequired(), Length(min=2, max=20)])
    user_last_name = StringField('Achternaam',
                           validators=[DataRequired(), Length(min=2, max=20)])
    user_email = StringField('Mail adres',
                           validators=[DataRequired(), Length(min=2, max=40)])

    user_vraag = RadioField("Een hele lange vraag", choices=['Geheel niet','Niet zo', 'Gemiddeld', 'Matig', 'Sterk of Ja!'])

#    email = StringField('Email',
#                        validators=[DataRequired(), Email()])
#    email = StringField('Email',
#                        validators=[DataRequired()])
#    password = PasswordField('Password', validators=[DataRequired()])
#    confirm_password = PasswordField('Confirm Password',
#                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Verzend')


#===========================================
# Hieronder is rechtstreeks van voorbeeld
#===========================================

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
#    email = StringField('Email',
#                        validators=[DataRequired(), Email()])
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
#    email = StringField('Email',
#                        validators=[DataRequired(), Email()])
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')