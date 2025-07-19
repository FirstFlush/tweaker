

normalize_testdata = [
    ("  Hello,   World!  ", "hello world"),
    ("Ｔｅｓｔ　ｓｔｒｉｎｇ！", "test string"),  # fullwidth chars → ascii
    ("𝓗𝓮𝓵𝓵𝓸     𝕎𝕠𝕣𝕝𝕕", "hello world"),  # fancy unicode fonts
    ("100% FREE!!!", "100 free"),
    ("  --dash--here--  ", "dash here"),
    ("🤖 Robots!    🛠️ Tools!", "robots tools"),
    ("e.g., i.e., etc.", "eg ie etc"),
    ("👨‍👩‍👧‍👦 family emoji test", "family emoji test"),
    ("CA$H mon€¥", "cah mon"),
    ("𝔘𝔫𝔦𝔠𝔬𝔡𝔢 𝔣𝔞𝔦𝔯𝔶𝔱𝔞𝔩𝔢", "unicode fairytale"),
    ("HELLO\tWORLD\n", "hello world"),  # tab and newline normalize to space
    ("  MULTIPLE     SPACES   HERE ", "multiple spaces here"),
    ("remove@all#symbols!", "removeallsymbols"),
    ("no-punctuation_should_remain", "no punctuation should remain"),
    ("This—dash—is—a—dash", "this dash is a dash"),
    ("☕ CAFE_MOOSE 🦌", "cafe moose"),
    ("___underscore___underscore_underscore___underscore___underscore", "underscore underscore underscore underscore underscore"),
    ("‐‑‒–—―−﹘﹣－_", ""),
    ("slash/and\\backslash", "slashandbackslash"),
]



punctuation_testdata = [
  ("this string ain't got punctuation, ok!", "this string aint got punctuation ok"),
  ("...wait—what?!", "waitwhat"),
  ("email@example.com", "emailexamplecom"),
  ("C++ > Java?", "C  Java"),
  ("123-456-7890", "1234567890"),
  ("it's 50% off—today only!!!", "its 50 offtoday only"),
  ("(brackets), [brackets], {brackets}", "brackets brackets brackets"),
  ("💯% guaranteed.", "guaranteed"),
  ("e.g., i.e., etc.", "eg ie etc"),
  ("she said, \"hello.\"", "she said hello"),
  ("use #hashtag & @mention", "use hashtag  mention"),
  ("--double dash-- test", "double dash test"),
  ("a.b.c.d", "abcd"),
  ("punctuation… ellipsis", "punctuation ellipsis"),
  ("he said—no way!", "he saidno way"),
  ("‘single’ and “double” quotes", "single and double quotes"),
  ("...leading, trailing...", "leading trailing"),
  ("mixed: punct!@#$%^&*()+[]{}|;:',.<>?/~`uation", "mixed punctuation"),
  ("🚀launch-ready!", "launchready"),
  ("math: 2*(3+4)-5=9", "math 23459")
]
