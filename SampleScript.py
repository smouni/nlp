import pickle
import os


dir_name = os.path.dirname(__file__)

def read_pickle_file(file_location= os.path.join(dir_name, 'dates_data_final.pickle') ):
    """

    :param file_location: Pass the location of the pickle file or put the pickle file in the same directory
    :return:
    """
    with open(file_location,'rb') as pickle_in:
        obj_struct = pickle.load(pickle_in)

        for id, multi_dates in obj_struct.items():
            print("id of the file ==>{0}\n".format(id))
            for date, date_features in multi_dates.items():
                print("date ==>{0}".format(date))
                text_on_left = date_features[0]
                text_on_right = date_features[1]
                number_of_times_date_repeated = date_features[2]
                is_date_relevant = date_features[3]
                print("text on the left ==>.{0}".format(text_on_left))
                print("text on the right ==>.{0}".format(text_on_right))
                print("number of times date is repeated ==>{0} ".format(number_of_times_date_repeated))
                print("is date relevant==>{0}\n".format(is_date_relevant))
            print("==== End of all dates in id {0}====== \n\n".format(id))


read_pickle_file()
