#!/usr/bin/env python

# Importing Modules #

# Declaring Constants #

#template_dot = { Discovery:[], Bulding:[], Combat:[], Health:[], Defense:[] }

# Defining Objects #
        
class Discovery(object):
    """Discovery Stats"""
    def __init__(self, a, b, c):
        super(Discovery, self).__init__()
        self.unique_h = ntab(a)
        self.discovered = ntab(b)
        self.xm_collected = ntab(c)

class Building(object):
    """Building Stats"""
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        super(Building, self).__init__()
        self.hacks = ntab(a)
        self.res_dep = ntab(b)
        self.links_c = ntab(c)
        self.control_f_c = ntab(d)
        self.mu_c = ntab(e)
        self.longest_link = ntab(f)
        self.largest_cf = ntab(g)
        self.xm_recharged = ntab(h)
        self.portals_c = ntab(i)
        self.unique_c = ntab(j)       

class Combat(object):
    """docstring for Combat"""
    def __init__(self, a, b, c, d):
        super(Combat, self).__init__()
        self.res_d = ntab(a)
        self.portals_d = ntab(b)
        self.links_d = ntab(c)
        self.cf_d = ntab(d)

class Health(object):
    """docstring for Health"""
    def __init__(self, a):
        super(Health, self).__init__()
        self.walked = ntab(a)
        
class Defense(object):
    """docstring for Defense"""
    def __init__(self, a, b, c, d, e):
        super(Defense, self).__init__()
        self.longest_p = ntab(a)
        self.longest_l = ntab(b)
        self.longest_ld = ntab(c)
        self.longest_cf = ntab(d)
        self.longest_cfd = ntab(e)
        
       
# Defining Functions #

def ntab(x):
    """Parse into tabbed stats"""
    return {'allTime': x[0], 'monthly': x[1], 'weekly':x[2]}

def get_data():
    """docstring for get_data"""
    pass

def process_data():
    """INPUT: chunk
       OUTPUT: Dictionary of Tuples
    """
    pass

# Defining main() #

def main():
    """docstring for main"""
    pass

#-- Runtime --#




#--   END   --#