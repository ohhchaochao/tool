data_init = [['1', '0', ' ', '3', 'a', ' ', '5', 'f', ' ', '6', 'e', ' ', '0', 'a', ' ', '0', '0', ' ', 'b', '0', ' ', '0',
            'c', '\n'],['1', '0', ' ', '3', 'a', ' ', '5', 'f', ' ', '6', 'e', ' ', '0', 'a', ' ', '0', '0', ' ', 'b', '0', ' ', '0',
            'c', '\n'],['1', '0', ' ', '3', 'a', ' ', '5', 'f', ' ', '6', 'e', ' ', '0', 'a', ' ', '0', '0', ' ', 'b', '0', ' ', '0',
            'c', '\n'],['1', '0', ' ', '3', 'a', ' ', '5', 'f', ' ', '6', 'e', ' ', '0', 'a', ' ', '0', '0', ' ', 'b', '0', ' ', '0',
            'c', '\n'],['1', '0', ' ', '3', 'a', ' ', '5', 'f', ' ', '6', 'e', ' ', '0', 'a', ' ', '0', '0', ' ', 'b', '0', ' ', '0',
            'c', '\n'],['1', '0', ' ', '3', 'a', ' ', '5', 'f', ' ', '6', 'e', ' ', '0', 'a', ' ', '0', '0', ' ', 'b', '0', ' ', '0',
            'c', '\n']]


def data_deal__():
    data_deal = []
    for m in range(len(data_init)):
        for n in range(len(data_init[m])):
            data_deal.append(data_init[m][n])
    print(data_deal)
    return data_deal


def to_ascii(data):
    data_deal_init = []
    data_deal_final = []
    list_data_deal = []
    i = 0
    while True:
        data_deal_init.append(data[i] + data[i + 1])
        i = i + 3
        if i + 1 > len(data):
            break
    with open("data.txt", "w", encoding='utf-8') as f:
        for i in range(len(data_deal_init)):
            data_deal_final.append(data_deal_init[i])
            list_data_deal.append(chr(int(data_deal_final[0], 16)))
            data_deal_final.clear()
            f.write(str(list_data_deal[i]))
        f.close()


if __name__ == "__main__":
    __data = data_deal__()
    to_ascii(__data)
