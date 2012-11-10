from functions import remove_duplicate_elements, remove_empty_elements

def generate_solutions(guess, feedback):

    def add_solution(colour, index, length):
        solution = []

        for i in range(index):
            solution.append('')

        solution.append(colour)

        for i in range(length - (index + 1)):
            solution.append('')

        return solution


    def add_correct_solution(guess):
        guess_length = len(guess)
        solutions = []

        for i in range(guess_length):
            solutions.append(add_solution(guess[i], i, guess_length))

        return solutions


    def add_partially_correct_solution(guess):
        guess_length = len(guess)
        solutions = []

        for i in range(guess_length):
            for j in range(guess_length):
                if guess[i] == guess[j]:
                    continue
                solutions.append(add_solution(guess[i], j, guess_length))

        remove_duplicate_elements(solutions)

        return solutions


    def add_empty_solution(length):
        solutions = []

        for i in range(length):
            solutions.append([])
            for j in range(length):
                solutions[i].append('')

        return solutions


    def merge_solutions(new_solutions, cumulative_solutions):
        solutions = []

        for new_solution in new_solutions:
            for cumulative_solution in cumulative_solutions:
                solution_length = len(new_solution)

                for i in range(solution_length):
                    if new_solution[i] != '' and cumulative_solution[i] == '':
                        solution = cumulative_solution[:]
                        solution[i] = new_solution[i]
                        solutions.append(solution)
                        break

        remove_duplicate_elements(solutions)

        return solutions


    def remove_invalid_solutions(guess, solutions):
        sorted_guess = sorted(guess)

        for i, solution in enumerate(solutions):
            if sorted(solution) != sorted_guess:
                solutions[i] = None

        remove_empty_elements(solutions)

        return solutions


    generate_solution = {'b': add_correct_solution, 'w': add_partially_correct_solution}

    guess_length = len(guess)
    solutions = add_empty_solution(guess_length)

    for key in feedback:
        solutions = merge_solutions(generate_solution[key](guess), solutions)

    solutions = remove_invalid_solutions(guess, solutions)

    return solutions
