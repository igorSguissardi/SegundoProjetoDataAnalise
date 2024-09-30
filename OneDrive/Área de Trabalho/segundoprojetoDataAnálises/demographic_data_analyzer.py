import pandas as pd



def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == "Bachelors"])

    # Calcular a porcentagem
    percentage_bachelors = (bachelors_count / total_people) * 100
    
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Definir filtros para educação avançada e não avançada
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # Filtrar pessoas que ganham mais de 50K
    high_income = df['salary'] == '>50K'

    # Calcular a porcentagem de pessoas com educação avançada que ganham mais de 50K
    higher_education_rich = (df[higher_education & high_income].shape[0] / df[higher_education].shape[0]) * 100

    # Calcular a porcentagem de pessoas sem educação avançada que ganham mais de 50K
    lower_education_rich = (df[lower_education & high_income].shape[0] / df[lower_education].shape[0]) * 100

    # Encontrar o número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Filtrar as pessoas que trabalham o número mínimo de horas
    min_workers = df[df['hours-per-week'] == min_work_hours]

    # Contar o número de pessoas que trabalham o mínimo de horas
    num_min_workers = min_workers.shape[0]

    # Calcular a porcentagem de pessoas que trabalham o mínimo de horas e ganham mais de 50K
    if num_min_workers > 0:
        rich_percentage = (min_workers[min_workers['salary'] == '>50K'].shape[0] / num_min_workers) * 100
    else:
        rich_percentage = 0  # Se não houver trabalhadores, a porcentagem é 0

    # Agrupar os dados pelo país e calcular as porcentagens de pessoas que ganham >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)

    # Calcular a porcentagem de pessoas que ganham >50K para cada país
    country_salary['percentage'] = country_salary['>50K'] * 100

    # Encontrar o país com a maior porcentagem de pessoas que ganham >50K
    highest_earning_country = country_salary['percentage'].idxmax()
    highest_earning_country_percentage = country_salary['percentage'].max()

   # Filtrar os dados para aqueles que ganham >50K e estão na Índia
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    # Encontrar a ocupação mais popular entre essas pessoas
    top_IN_occupation = india_high_income['occupation'].mode()[0] if not india_high_income.empty else None
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
