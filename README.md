# SecretHitler-SMS-Role-Assigner

An SMS service that can be used to privately assign roles to players via text message while playing the popular board game [Secret Hitler](https://www.secrethitler.com/). The game is typically played by passing out brown envelopes with cards inside that describe the hidden identity of each player. Every player then looks at their role privately, all players close their eyes, and someone will then instruct the Fascist players to open their eyes or raise their hand to share the necessary pre-game information. This project solves two slight inconveniences with this process:
1. The eye closing and opening process gets quite tedious and annoying when playing many rounds.
2. The brown envelopes are made out of paper and inevitably get creased or wet in memorable ways, making it harder to keep roles a secret, and often requiring players to hide their envelope.

After initial configuration, the service will allow any player to simply text the word `assign` and all players will receive a text message with the information they should know before the game begins. For example:
- `Your role is liberal.`
- `Your role is fascist. Fascists are: (Alice is fascist) (Bob is hitler)`

The service also provides functionality for the **_Investigate Party Membership_** president power where the president can look at any player's party membership card. At this point in the game, the president will simply send `View Charlie`, and will receive a text message in return `Charlie's party is liberal`. Everyone else in the game will receive a text `Charlie's party membership was viewed.` to ensure players cannot secretly view each others cards.

These two simple features allow the game to be played seamlessly without using the brown envelopes at all, and forgoing the eye closing ritual at the beginning of each round.

## Perform the following once to get started:
1. Create a free account and phone number with Twilio.
2. Put your Twilio phone number SID, and Auth Token in a `.env` file to be accessed as follows (or just paste it into the code if you're keeping it locally):
    ```python
    phone_number = os.environ.get("TWILIO_PHONE_NUM")
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    ```
3. Verify each player's phone number in the Twilio console by clicking "Add a new Caller ID".
4. Install dependencies:
    ```bash
    pip install twilio
    pip install python-dotenv
    ```

## Each session:
1. run python main.py. Leave it running for the whole session (or serve it elsewhere to run continuously).
2. anyone text "hello" to your twilio phone number
3. each player text "add (their name)" to your twilio phone number. All information will be passed to and from players with this phone number.
4. after all players are added, anyone text "start game"
   
## Each round:
1. anyone text `assign`. new roles will be generated and texted to everyone.
2. to enact the **_Investigate Party Membership_** president power, the president simply texts `View Bob`.
3. at any point if you need to change the player configuration, anyone can text `end game` to restart from _**Each session**_.

## Summary of Commands:
all commands are case insensitive.
- `hello`: start listening to add players. state: 'inactive' -> 'adding players'
- `add Alice`: add player called Alice.
- `start game`: done adding players. state: 'add players' -> 'active'
- `assign`: get new roles to start a new round.
- `view Eve`: view Eve's party membership. notifies other players that Eve's membership was viewed.
- `end game`: end the current sesssion to restart with new players. state: any -> 'inactive'
