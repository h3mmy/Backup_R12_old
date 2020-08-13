#!/usr/bin/env runhaskell

{-
 *  ingress.hs
 *  
 *
 *  Created by Zachariah Aslam on Dec 31, 2013.
 *  Copyright 2014 "XaC. IM". All rights reserved.
 *
-}
{-
putStrLn "Total # of Hacks: "
hacks_t <- getLine 
putStrLn "Total Resonators deployed: "
res_dep <- getLine
putStrLn "Total Resonators destroyed: "
res_d <- getLine
putStrLn "Links Created: "
links_c <- getLine
putStrLn "Links Destroyed: "
links_d <- getLine
putStrLn "Control Fields Created: "
cf_create <- getLine
putStrLn "Control Fields Destroyed: "
cf_destroy <- getLine
putStrLn "New Portals Discovered: "
new_p_discovered <- getLine
putStrLn "Portal Pictures Accepted: "
n_picture_accepted <- getLine
putStrLn "Total AP: "
ap <- getLine
-}

-- ap = 100*hacks_e + 0*hacks_f + 10*n_recharge + 500*p_capture + 125*res_dep + 75*res_d + 250*p_complete + 0*up_own_res + 65*up_oth_res + 313*links_c + 187*links_d + 1250*cf_create + 750*cf_destroy + 125*mods + 1000*new_p_discovered + 500*n_picture_accepted

-- 2 pictures accepted. (Zak)

hacks_t = 2231
res_dep = 1614
res_d = 788
links_c = 131
links_d = 196
cf_create = 47
cf_destroy = 140
new_p_discovered = 6
n_picture_accepted = 2
ap = 751409

k_ap = 125*res_dep + 75*res_d + 1250*cf_create + 750*cf_destroy + 1000*new_p_discovered + 500*n_picture_accepted

