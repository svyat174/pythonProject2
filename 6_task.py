violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

xxx = violator_songs_list[3][1]
yyy = violator_songs_list[5][1]
zzz = violator_songs_list[8][1]

summ_3 = xxx + yyy + zzz

print('Три песни звучат', round(summ_3, 3), 'минут')

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

xxx_1 = violator_songs_dict['Sweetest Perfection']
yyy_2 = violator_songs_dict['Policy of Truth']
zzz_3 = violator_songs_dict['Blue Dress']

summ_33 = xxx_1 + yyy_2 + zzz_3

print('А другие три песни звучат', round(summ_33, 3), 'минут')
