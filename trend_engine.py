import pandas as pd
from pytrends.request import TrendReq
import requests
import time

class TrendEngine:
    def __init__(self):
        # Connect to Google
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def get_google_trends(self, keyword):
        """Fetches interest over time from Google Trends (Last 12 Months)."""
        try:
            self.pytrends.build_payload([keyword], cat=0, timeframe='today 12-m')
            # Add a small delay to avoid rate limiting
            time.sleep(1) 
            data = self.pytrends.interest_over_time()
            if data.empty:
                return pd.DataFrame()
            return data.drop(columns=['isPartial'], errors='ignore')
        except Exception as e:
            print(f"Error fetching Google Trends: {e}")
            return pd.DataFrame()

    def get_hacker_news_mentions(self, keyword):
        """Fetches mentions of keyword in Hacker News stories (Last 100 hits)."""
        url = f"http://hn.algolia.com/api/v1/search_by_date?query={keyword}&tags=story&hitsPerPage=100"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"HN API Error: {response.status_code}")
                return pd.DataFrame()
                
            data = response.json()
            hits = data.get('hits', [])
            if not hits:
                return pd.DataFrame()
            
            # Process to dataframe
            df = pd.DataFrame(hits)
            df['created_at'] = pd.to_datetime(df['created_at'])
            # Group by date
            daily_counts = df.groupby(df['created_at'].dt.date).size().to_frame(name='hn_mentions')
            daily_counts.index = pd.to_datetime(daily_counts.index)
            return daily_counts
        except Exception as e:
            print(f"Error fetching Hacker News: {e}")
            return pd.DataFrame()

    def get_x_trends(self, keyword):
        """Fetches recent X.com (Twitter) posts via Nitter (ntscraper)."""
        try:
            from ntscraper import Nitter
            scraper = Nitter(log_level=1, skip_instance_check=False) 
            # Search for the keyword
            print(f"🐦 Searching X.com for: {keyword}")
            tweets = scraper.get_tweets(keyword, mode='term', number=10)
            
            data = []
            if tweets and 'tweets' in tweets:
                for tweet in tweets['tweets']:
                    data.append({
                        "text": tweet['text'],
                        "date": tweet['date'],
                        "likes": tweet['stats']['likes'],
                        "retweets": tweet['stats']['retweets'],
                        "link": tweet['link']
                    })
            if not data:
                return pd.DataFrame()
            return pd.DataFrame(data)
        except Exception as e:
            print(f"❌ X.com Error: {e}")
            return pd.DataFrame()

    def get_rss_trends(self, keyword):
        """Extracts trends from RSS feeds (Subreddits, News, etc.)"""
        import feedparser
        feeds = [
            f"https://www.reddit.com/search.rss?q={keyword}&sort=new",
            f"https://hnrss.org/newest?q={keyword}",
            f"https://news.google.com/rss/search?q={keyword}"
        ]
        
        all_entries = []
        for url in feeds:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:5]: # Top 5 from each
                    all_entries.append({
                        "title": entry.title,
                        "link": entry.link,
                        "published": getattr(entry, 'published', 'N/A'),
                        "source": url.split('/')[2]
                    })
            except Exception as e:
                print(f"RSS Error: {e}")
        
        return pd.DataFrame(all_entries)

if __name__ == "__main__":
    eng = TrendEngine()
    print("Fetching Google Trends for 'AI'...")
    print(eng.get_google_trends("AI").tail())
    print("\nFetching HN Mentions for 'AI'...")
    print(eng.get_hacker_news_mentions("AI").tail())
    print("\nFetching X.com Trends for 'AI'...")
    print(eng.get_x_trends("AI").head())
