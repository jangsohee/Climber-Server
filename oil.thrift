namespace java oil_climber

struct SimilarImg {
  1: string imgUrl,
  2: string linkUrl
}

struct MatchingPage {
  1: string title,
  2: string imgUrl,
  3: string linkUrl,
  4: string content
}

struct ImgSearchResult {
  1: string guess,
  2: list<SimilarImg> imgs,
  3: list<MatchingPage> pages
}

service Oil {
    ImgSearchResult imgSearch(1:string img)
}

