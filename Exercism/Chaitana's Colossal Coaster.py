# Chaitana's Colossal Coaster
# https://exercism.org/tracks/python/exercises/chaitanas-colossal-coaster

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    return queue.count(person_name)


def remove_the_last_person(queue):
    return queue.pop()


def sorted_names(queue):
    return sorted(queue)


print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"))
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"))
print(find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve"))
print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky"))
print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"))
print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"))
print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))
print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))
