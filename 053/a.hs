main :: IO ()
main = do
  x <- readLn :: IO Int
  putStrLn $ if x < 1200 then "ABC" else "ARC"
