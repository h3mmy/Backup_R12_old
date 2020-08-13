{-
 *  graph1.hs
 *  
 *
 *  Created by Zachariah Aslam on Sep 26, 2013.
 *  Copyright 2013 "XaC. IM". All rights reserved.
 *
-}

#!/usr/bin/env runhaskell

-- Purpose: Translate Yaml input -> Database Entry Nodes as Output
-- Caveats: Cannot access database. May access a database template if needed (make a file for it [tag:todo])

version = "0.0.1"


import qualified Data.Yaml as Yml

