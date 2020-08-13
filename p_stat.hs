#!/usr/bin/env runhaskell

{-
 *  p_stat.hs
 *  
 *
 *  Created by Zachariah Aslam on Dec 24, 2013.
 *  Copyright 2013 "XaC. IM". All rights reserved.
 *
-}

{-# OPTIONS_GHC -XMultiParamTypeClasses #-}

newtype Name = Name String

data Contact_info = Contact_info {
								phoneNumber :: Int
								}


class Money a c where
	f :: a -> Float
	g :: c -> [Char]



data Person = Person {
					name :: Name,
					contactData :: Contact_info,
					balance :: Float,
					hold :: Bool,
					account_id :: Int
					} 
	