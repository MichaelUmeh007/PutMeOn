from data_access import *


if __name__ == '__main__':
    top = get_recc_data()
    get_recommendations(top)