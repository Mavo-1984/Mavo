def simulation(m):
    result = []
    for j in range(m):
        random.seed(48 + j)
        student = make_stu(n, m)
        univ = univ_make(df)

        for i in range(150):
            da(student, univ)
            result.append(len(np.where(student[:, 3] == 0)[0]))
    resultnp = np.array(result)
    resultnp.reshape(m, 150)

    return resultnp
