
import searchtweets
from searchtweets import load_credentials, ResultStream, gen_rule_payload, collect_results

premium_search_args =  load_credentials(filename="./twitter_keys.yaml", 
                                        yaml_key="search_tweets_api", 
                                        env_overwrite=False)
rule = gen_rule_payload("#MedicaidCoversUs @ACSCANAL",
                        from_date="2019-04-01",
                        to_date="2019-11-30",
                        results_per_call=100)
#rule: from:ACSCANAL to:ACSCANAL @ACSCANAL

tweets = collect_results(rule,
                        max_results=100,
                        result_stream_args=premium_search_args)

[print(tweet.all_text, end='\n\n') for tweet in tweets[0:100]]
[print(tweet.created_at_datetime, end='\n\n') for tweet in tweets[0:100]]

