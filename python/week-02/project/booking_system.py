__contributor__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

movie_list_onshow = [
        {
        'The Matrix': {
            'genre': 'Action',
            'show_times': {
                'start_time': '09:00',
                'ticket_price': 15.00,
                'seats_number': 100
            },
            'show_times': {
                'start_time': '12:00',
                'ticket_price': 15.00,
                'seats_number': 100
            },
        },
    }
]

snack_bar_list = {
    'Popcorn Small': 5.00,
    'Popcorn Medium': 7.00,
    'Popcorn Large': 9.00,
    'Nachos': 7.00,
    'Soda': 3.00,
    'Candy': 2.00,
    'Chocolate': 4.00,
    'Ice Cream': 6.00,
    'Cola': 3.00,
    'water': 1.00,
    'tea': 2.00,
}

order_information = {
    'customer_name': '',
    'movie_names': '',
    'movie_show_time': '',
    'ticket_quantity': 0,
    'snacks': [],
    'cost_of_snacks': 0.00,
    'cost_of_tickets': 0.00,
    'subtotal': 0.00,
    'cost_of_fees': 0.00,
    'total_amount': 0.00,
}

past_customer_orders = []

#filter func ile yapila bilir
#Someone searches for a genre we don't currently have any movies in — this should just show "no results," not break the program
#Instead, the program should show a short, clear message explaining what went wrong.
def filter_movies_by_genre(genre):

    return 0

#filter func ile yapila bilir
#Instead, the program should show a short, clear message explaining what went wrong.
def filter_movies_by_ticket_price(ticket_price):

    return 0

def calculate_total_cost_of_tickets(ticket_quantity, ticket_price):

    return 0

def calculate_total_cost_of_snacks(snack_list):

    return 0

def calculate_total_cost_of_fees(cost_of_tickets, cost_of_snacks):

    return 0

def calculate_total_cost_of_booking(cost_of_tickets, cost_of_snacks, cost_of_fees):

    return 0

#Someone tries to book more seats than are actually available.
#Instead, the program should show a short, clear message explaining what went wrong.
def update_movie_list(movie_name, show_time, ticket_quantity):

    return 0

def booking_ticket():
    movie_name = input('Enter the movie name to book a ticket: ')

    #Someone enters a customer or movie that doesn't exist in the system.
    if(movie_name not in [movie for movie_dict in movie_list_onshow for movie in movie_dict]):
        print(f'Movie "{movie_name}" is not available in the movie list.')
        return 0

    show_time = input('Enter the show time (HH:MM) to book a ticket: ')

    #someone enters a show time that doesn't exist for the selected movie.
    if show_time not in [show_time for movie_dict in movie_list_onshow for movie in movie_dict[movie_name]['show_times']]:
        print(f'Show time "{show_time}" is not available for movie "{movie_name}".')
        return 0
    
    ticket_quantity = int(input('Enter the number of tickets to book: '))

    if ticket_quantity > movie_list_onshow[0][movie_name]['show_times'][show_time]['seats_number']:
        print(f'Cannot book {ticket_quantity} tickets. Only {movie_list_onshow[0][movie_name]["show_times"][show_time]["seats_number"]} seats are available.')
        return 0

    update_movie_list(movie_name, show_time, ticket_quantity)
    
    return 0

#Someone tries to check out an order that has no movie selected yet.
#Instead, the program should show a short, clear message explaining what went wrong.
def check_out_order(order_information):

    return 0

def print_snack_bar_list(snack_bar_list):

    return 0


def take_snack_order():
    order_snacks = []
    while True:
        print_snack_bar_list(snack_bar_list)

        snack_name = input('Enter the snack name to order (or type "done" to finish): ')

        if snack_name.lower() == 'done':
            break
        if snack_name.lower() not in snack_bar_list:
            print(f'Snack "{snack_name}" is not available in the snack bar list.')
            continue

        snack_quantity = int(input('Enter the quantity of the snack to order: '))

        order_snacks.append({
            'snack_name': snack_name, 
            'snack_quantity': snack_quantity
            })

    return order_snacks


#Instead, the program should show a short, clear message explaining what went wrong.
print('Welcome to the Movie Booking System!')

while True:
    user_selection = input("""
        Please select an option:
            1. Filter movies by genre
            2. Filter movies by ticket price
            3. Book a ticket
            4. Order snacks
            5. Check out order
            6. Exit
    """)

    if(user_selection == '1'):
        genre = input('Enter a genre to filter movies: ')
        filtered_movies = filter_movies_by_genre(genre, movie_list_onshow)

        print(f'Filtered movies by genre "{genre}": {filtered_movies}')
    elif(user_selection == '2'):
        ticket_price = float(input('Enter a ticket price to filter movies: '))
        filtered_movies = filter_movies_by_ticket_price(ticket_price, movie_list_onshow)

        print(f'Filtered movies by ticket price "{ticket_price}": {filtered_movies}')
    elif(user_selection == '3'):
        booking_ticket()
    elif(user_selection == '4'):
        order_snacks_list = take_snack_order()

        if len(order_snacks_list) == 0:
            print('No snacks were ordered.')
        else:
            calculate_total_cost_of_snacks(order_snacks_list)
    elif(user_selection == '5'):
        check_out_order(order_information)
    elif(user_selection == '6'):
        print('Exiting the Movie Booking System. Goodbye!')
        break    