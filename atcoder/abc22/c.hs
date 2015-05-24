-- できてない
main = do
  [n, m] <- fmap (read :: String -> Int) . words <$> getLine
  as <- fmap fmap (read :: String -> Int) . words <$> replicateM m getLine
