LL_UID=$1
LL_CONTENT=$2
LL_TOKEN=$3
 
echo "-----------------UID" $LL_UID
echo "-----------------CONTENT" $LL_CONTENT
echo "-----------------TOKEN" $LL_TOKEN

curl -X POST \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer '$LL_TOKEN'' \
-d '{
        "to": ["'$LL_UID'"],
        "messages":[
              {
                    "type":"text",
                    "text":"'$LL_CONTENT'"
              }
        ]
}' https://api.line.me/v2/bot/message/multicast
