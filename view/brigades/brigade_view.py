
def brigade_bttln_Lists(brigade_number: int, presenter, brgdCmndr, brgdBattalionsList):
    """

    :param brigade_number: brigade number in the division list
    :param presenter: presenter object
    :param brgdCmndr: GUI combo box for brigade commander names
    :param brgdBattalionsList: list of GUI combo boxes for battalions name showing
    :return: fill GUI combo boxes lists for chosen brigade commander and battalions variants
    """
    # задаем возможны варианты имен командиров

    if brgdCmndr != None:
        cmndrs_list = presenter.BrigadeCmndrsNamesList(brigade_number)
        for cmndrName in cmndrs_list:
            brgdCmndr.addItem(cmndrName)
    # задаем возможные варианты для батальона

    for i in range (0, len(brgdBattalionsList)):

        bttln_list = presenter.BrigadeBttlnList(i, brigade_number)
        for bttlnName in bttln_list:
            brgdBattalionsList[i].addItem(bttlnName)




