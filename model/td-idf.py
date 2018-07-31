# Calculate IDF
tot = len(df['docIdx'].unique())
pb_ij = df.groupby(['wordIdx'])
IDF = np.log(tot / pb_ij['docIdx'].count())
IDF_dict = IDF.to_dict()


def MNB(df, smooth=False, IDF=False):
    '''
    Multinomial Naive Bayes classifier
    :param df [Pandas Dataframe]: Dataframe of data
    :param smooth [bool]: Apply Smoothing if True
    :param IDF [bool]: Apply Inverse Document Frequency if True
    :return predict [list]: Predicted class ID
    '''
    # Using dictionaries for greater speed
    df_dict = df.to_dict()
    new_dict = {}
    prediction = []

    # new_dict = {docIdx : {wordIdx: count},....}
    for idx in range(len(df_dict['docIdx'])):
        docIdx = df_dict['docIdx'][idx]
        wordIdx = df_dict['wordIdx'][idx]
        count = df_dict['count'][idx]
        try:
            new_dict[docIdx][wordIdx] = count
        except:
            new_dict[df_dict['docIdx'][idx]] = {}
            new_dict[docIdx][wordIdx] = count

    # Calculating the scores for each doc
    for docIdx in range(1, len(new_dict) + 1):
        score_dict = {}
        # Creating a probability row for each class
        for classIdx in range(1, 21):
            score_dict[classIdx] = 1
            # For each word:
            for wordIdx in new_dict[docIdx]:
                # Check for frequency smoothing
                # log(1+f)*log(Pr(i|j))
                if smooth:
                    try:
                        probability = Pr_dict[wordIdx][classIdx]
                        power = np.log(1 + new_dict[docIdx][wordIdx])
                        # Check for IDF
                        if IDF:
                            score_dict[classIdx] += (
                                    power * np.log(
                                probability * IDF_dict[wordIdx]))
                        else:
                            score_dict[classIdx] += power * np.log(
                                probability)
                    except:
                        # Missing V will have log(1+0)*log(a/16689)=0
                        score_dict[classIdx] += 0
                        # f*log(Pr(i|j))
                else:
                    try:
                        probability = Pr_dict[wordIdx][classIdx]
                        power = new_dict[docIdx][wordIdx]
                        score_dict[classIdx] += power * np.log(
                            probability)
                        # Check for IDF
                        if IDF:
                            score_dict[classIdx] += power * np.log(
                                probability * IDF_dict[wordIdx])
                    except:
                        # Missing V will have 0*log(a/16689) = 0
                        score_dict[classIdx] += 0
                        # Multiply final with pi
            score_dict[classIdx] += np.log(pi[classIdx])

            # Get class with max probabilty for the given docIdx
        max_score = max(score_dict, key=score_dict.get)
        prediction.append(max_score)

    return prediction