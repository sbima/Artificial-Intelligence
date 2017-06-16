# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:09:41 2016

@author: Shivuu
"""

min_value = min(words_dic.values())         #['AFT', 'LEE']
                        print min_value

                        result = [key for key, value in words_dic.iteritems() if value == min_value] #[6,7]
                        print result