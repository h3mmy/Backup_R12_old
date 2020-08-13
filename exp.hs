#!/usr/bin/env runhaskell

{-
 *  exp.hs
 *  
 *
 *  Created by Zachariah Aslam on Oct 7, 2013.
 *  Copyright 2013 "XaC. IM". All rights reserved.
 *
-}

newtype Price = Float | Int

data Gooball = {Item :: String
               ,Increment :: Int | [Int] 
			   ,I_unit :: Char:'g'
			   ,Ask :: Price
			   ,Bid :: Price
			   } deriving (Show, Read)
