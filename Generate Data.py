from faker import Faker
import random
import pandas as pd


# Generates a random ID number of specified length.
def generate_id(digits):
    lowerLim = int('1' + (digits - 1)*'0')
    upperLim = int(digits*'9')
    id = random.randint(lowerLim, upperLim)
    return id


generate = Faker()

# Creates a fake profile including first name, last name, email address, and a security question and answer. The
# four options for security questions are city of birth, mother's maiden name, dream job, and favorite movie (taken
# from the sign-up page of Barnes and Noble's website).
def fake_user():
    user_df = pd.DataFrame()

    user_id = generate_id(8)
    for instance in range(50):
        lname = generate.last_name()
        fname = generate.first_name()
        email = (fname[:1] + lname + random.choice(['@gmail.com', '@yahoo.com', '@aol.com', '@hotmail.com']).lower())
        pw = generate.password()

        securitynum = random.randrange(1,5)
        if securitynum == 1:
            securitya = generate.city()  # returns city you were born in
        elif securitynum == 2:
            securitya = generate.last_name()  # returns mother's maiden name
        elif securitynum == 3:
            securitya = generate.job()  # returns dream job
        else:
            securitya = random.choice(['Shrek', 'Shrek 2', 'Bee Movie'])  # returns favorite movie

        new_row = {'User_ID':f'{user_id:.0f}', 'First_Name':fname, 'Last_Name':lname, 'Email':email,
                   'Password':pw, 'Security Question':securitya}
        user_df = user_df.append(new_row, ignore_index=True)

        user_id += 1
    return user_df

user_table = fake_user()
print(user_table)


# Export generated data as csv file
def export(df):
    df.to_csv('user_data.csv')

export(user_table)
