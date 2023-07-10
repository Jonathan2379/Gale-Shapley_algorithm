def gale_shapley(men_preferences, women_preferences):
    n = len(men_preferences)  # /pega o tamanho de preferencias dos homens
    # cria um array de -1 do tamanho das preferencias
    homens_options = [-1] * n
    mulheres_options = [-1] * n
    men_index = [0] * n  # cria um index de 0 do tamanho das preferencias

    # verifica se ainda existem homens não engajados.
    while homens_options.count(-1) > 0:
        # Se ainda houver valores "-1" na lista, significa que há homens não engajados e o loop continuará.
        free_man = homens_options.index(-1)
        woman = men_preferences[free_man][men_index[free_man]]
        men_index[free_man] += 1

        if mulheres_options[woman] == -1:
            homens_options[free_man] = woman
            mulheres_options[woman] = free_man
        else:
            current_man = mulheres_options[woman]
            if women_preferences[woman].index(current_man) > women_preferences[woman].index(free_man):
                homens_options[current_man] = -1
                homens_options[free_man] = woman
                mulheres_options[woman] = free_man

    return homens_options, mulheres_options


# Exemplo de uso
men_preferences = [
    [1, 0, 2, 3],
    [3, 1, 0, 2],
    [0, 1, 2, 3],
    [1, 0, 3, 2]
]

women_preferences = [
    [2, 3, 1, 0],
    [0, 1, 2, 3],
    [2, 1, 3, 0],
    [0, 1, 2, 3]
]

men_engaged, women_engaged = gale_shapley(men_preferences, women_preferences)

print("Homens Engajados:", men_engaged)
print("Mulheres Engajadas:", women_engaged)
