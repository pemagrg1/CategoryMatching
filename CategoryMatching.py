from modules import semanticMapping, wupAlgo,wupAndPath
# from modules import categoryMatchingUsingGensim


class CategoryMatching:
    def __init__(self):
        pass

    def match(self, str1,str2, method):
        """
        :param method:
            Methods availabel are:
                gensim:
                wup:
                wup_path:
                semantic:

        :return:
        """

        if method != None:
            if method == "gensim":
                pass
            elif method == "wup":
                return wupAlgo.wup_similarity(str1,str2)
            elif method == "wup_Path":
                return wupAndPath.wupAndPathMapping(str1,str2)
            elif method == "semantic":
                return semanticMapping.semanticSimilarityMapping(str1,str2)
        else:
            return "please specify the method gensim,wup,wup_path,or semantic"





c = CategoryMatching()
print (c.match("Cajun Restaurant","Restaurant",method="wup_Path"))
