# misc
"""
Class() -> obj                                  Class.__init__(self) -> obj                             create new obj
repr(obj) -> str                                Class.__repr__(self) -> str                             repr of obj
str(obj) -> str                                 Class.__str__(self) -> str                              str of obj
hash(obj) -> int                                Class.__hash__(self) -> int                             hash of obj
obj.copy() -> obj                               Class.copy(self) -> obj                                 create a copy of obj
Class.from_json(dict) -> obj                    Class.from_json(cls, dict) -> obj                       convert jsondict to obj
obj.to_json() -> dict                           Class.to_json(self) -> dict                             convert obj to jsondict
"""

# container
"""
obj + other -> obj                              Class.__add__(self, other) -> obj                       combine two containers
other + obj -> obj                              Class.__radd__(self, other) -> obj                      combine two containers
obj += other -> None                            Class.__iadd__(self, other) -> None                     combine two containers (in-place)
elem in obj -> bool                             Class.__contains__(self, other) -> bool                 check if elem [element] is in obj [container]
len(obj) -> int                                 Class.__len__(self) -> int                              count number of elements in container
"""

# math
"""
obj + other -> obj                              Class.__add__(self, other) -> obj                       add two numbers together
other + obj -> obj                              Class.__radd__(self, other) -> obj                      add two numbers together
obj += other -> None                            Class.__iadd__(self, other) -> obj                      add two numbers together (in-place)
obj - other -> obj                              Class.__sub__(self, other) -> obj                       subtract other [number] from obj [number]
other - obj -> obj                              Class.__rsub__(self, other) -> obj                      subtract obj [number] from other [number]
obj -= other -> None                            Class.__isub__(self, other) -> obj                      subtract other [number] from obj [number] (in-place)
"""

# math comparison (see @total_ordering)
"""
obj < other -> bool                             Class.__lt__(self, other) -> bool                       obj is less than other
obj <= other -> bool                            Class.__le__(self, other) -> bool                       obj is less than or equal to other
obj == other -> bool                            Class.__eq__(self, other) -> bool                       obj is equal to other
obj != other -> bool                            Class.__ne__(self, other) -> bool                       obj is not equal to other
obj > other -> bool                             Class.__gt__(self, other) -> bool                       obj is greater than other
obj >= other -> bool                            Class.__ge__(self, other) -> bool                       obj is greater than or equal to other
"""

# set
"""
len(obj) -> int                                 Class.__len__(self) -> int                              count number of elements in obj [set]
elem in obj -> bool                             Class.__contains__(self, other) -> bool                 check if elem [element] is in obj [set]

obj.isdisjoint(other) -> bool                   Class.isdisjoint(self, other) -> bool                   check if obj [set] has no elements in common with other [set]
obj.issubset(other) -> bool                     Class.issubject(self, other) -> bool                    check if all elements in obj [set] are in other [set]
obj <= other -> bool                            Class.__le__(self, other) -> bool                       check if all elements in obj [set] are in other [set]
obj < other -> bool                             Class.__lt__(self, other) -> bool                       check if all elements in obj [set] are in other [set] but they are not equal
obj.issuperset(other) -> bool                   Class.issuperset(self, other) -> bool                   check if all elements in other [set] are in obj [set]
obj >= other -> bool                            Class.__ge__(self, other) -> bool                       check if all elements in other [set] are in obj [set]
obj > other -> bool                             Class.__gt__(self, other) -> bool                       check if all elements in other [set] are in obj [set] but they are not equal

obj.union(*others) -> obj                       Class.union(self, *others) -> obj                       return a new set with elements from obj [set] and all others [sets]
obj | other -> obj                              Class.__or__(self, other) -> obj                        return a new set with elements from obj [set] and other [set]
obj.intersection(*others) -> obj                Class.intersection(self, *others)                       return a new set with elements common to obj [set] and all others [sets]
obj & other -> obj                              Class.__and__(self, other) -> obj                       return a new set with elements common to obj [set] and other [set]
obj.difference(others) -> obj                   Class.difference(self, others) -> obj                   return a new set with elements in obj [set] that are not in the others [sets]
obj - other -> obj                              Class.__sub__(self, other) -> obj                       return a new set with elements in obj [set] that are not in other [set]
obj.symmetric_difference(other) -> obj          Class.symmetric_difference(self, other) -> obj          return a new set with elements in either obj [set] or other [set] but not both
obj ^ other -> obj                              Class.__xor__(self, other) -> obj                       return a new set with elements in either obj [set] or other [set] but not both

obj.update(*others) -> None                     Class.update(self, *others) -> None                     update obj [set], adding elements from all others [sets] (in-place)
obj |= other -> None                            Class.__ior__(self, other) -> None                      update obj [set], adding elements from other [set] (in-place)
obj.intersection_update(*others) -> None        Class.intersection_update(self, *others) -> None        update obj [set], keeping only elements found in obj [set] and all others [sets] (in-place)
obj &= other -> None                            Class.__iand__(self, other) -> None                     update obj [set], keeping only elements found in obj [set] and other [set] (in-place)
obj.difference_update(*others) -> None          Class.difference_update(*others) -> None                update obj [set], removing elements found in others [sets] (in-place)
obj -= other -> None                            Class.__isub__(self, other) -> None                     update obj [set], removing elements found in other [set] (in-place)
obj.symmetric_difference_update(other) -> None  Class.symmetric_difference_update(self, other) -> None  update obj [set], keeping only elements found in either obj [set] or other [set], but not in both
obj ^= other -> None                            Class.__ixor__(self, other) -> None                     update obj [set], keeping only elements found in either obj [set] or other [set], but not in both

obj.add(elem) -> None                           Class.add(self, elem) -> None                           add elem [element] to obj [set]
obj.remove(elem) -> None                        Class.remove(self, elem) -> None                        remove elem [element] from obj [set], raises KeyError if elem [element] is not contained in obj [set]
obj.discard(elem) -> None                       Class.discard(self, elem) -> None                       remove elem [element] from obj [set] if it is present
obj.pop() -> elem                               Class.pop(self) -> elem                                 remove and return an arbitrary element from obj [set], raises KeyError if obj [set] is empty
obj.clear() -> None                             Class.clear(self) -> None                               remove all elements from obj [set]
"""
