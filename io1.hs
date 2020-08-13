#!/usr/bin/env runhaskell
{-# OPTIONS_GHC -O2 -llvm #-}
{-
 *  io1.hs
 *  
 *
 *  Created by Zachariah Aslam on Jan 4, 2014.
 *  Copyright 2014 "XaC. IM". All rights reserved.
 *
-}

import Control.Monad
import Data.Char (isDigit)

version = "0.0.1"


phone_number_pure :: [Char] -> Bool
phone_number_pure hi_phone = and [(length hi_phone == 10), and $ map isDigit hi_phone]




main = interact $ show $ phone_number_pure $ concat $ words $ lines
	