# -*- coding: utf-8 -*-
"""
Class in charge of giving SRT format to Dialog objects and writing them to a
final SRT file.
"""


class WriterSrt(object):
    """
    Class to convert and write data in SRT format.
    """

    def write(
        self,
        filename: str = None,
        data: str = None
    ) -> None:
        """
        Write data into SRT file.
        """
        with open(filename, 'w') as file:
            file.writelines(data)

    def convertData(
        self,
        data: list
    ) -> str:
        """
        Converts data from a list of object Dialog to SRT format.
        """
        if data != []:
            string_script = ""
            for i in range(len(data)):
                objDialog = data[i]
                string_script += "{0}\n{1}\n{2}\n\n".format(
                    i + 1,
                    self.__format_timestamp(objDialog),
                    objDialog.dialog
                )
                # print(string_script)
            return string_script
        else:
            return ''

    def __format_timestamp(self, item) -> str:
        """
        Formats start and end timestamps.
        """
        return "{0} --> {1}".format(item.time_start, item.time_end)
