from flask import Flask
import random

app = Flask(__name__)

@app.route('/beer-joke', methods=['GET'])
def beer_joke():
    jokes = [
        "A Roman walks into a bar. He holds up two fingers and says “give me five beers.’’",
        "A skeleton walks into a bar. Orders a beer and a mop.",
        "I fear my last words will be ‘‘hold my beer and watch this.’’",
        "Why do they never serve beer at a math party? – Because you can’t drink and derive.",
        "A neutron walks into a bar and asks, “how much for a beer?” The bartender replies, “for you? No charge!”",
        "Trust me, you can dance. – Beer",
        "What did the bottle write on the postcard? Wish you were beer!",
        "IPA a lot when I drink beer.",
        "Never look at your beer as half empty. Look at it as halfway to your next beer.",
        "What is the definition of a balanced diet? A beer in each hand.",
        "What’s the difference between Bud Light and having sex in a Kayak? They’re both f*cking close to water!",
        "How does a man show that he is planning for the future? He buys two cases of beer.",
        "What do you never say to a policeman? “Sure let me grab my license. Can you hold my beer?”",
        "This beer tastes like I’m not going to work tomorrow.",
        "What did the beer sing on the beach? “Don’t worry. Be hoppy.”",
        "Beer…because you can’t drink bacon.",
        "“Friends bring happiness into your life. Best friends bring beer.”",
        "One beer, two beer, three beer, four. Then I hit the floor.",
        "Roses are red, violets are blue. Poems are hard. Beer!",
        "They say you can’t find happiness at the bottom of a beer. No kidding, who’s happy when their beer is over?",
        "When my friend fell asleep at the bar I poured ale at him. It was a brewed awakening.",
        "Hey bartender, I need a beer. I’ve got way too much blood in my alcohol system.",
        "Guy walks into a bar, orders a beer. As the bartender hands it to him, the guy realizes he really has to take a leak urgently. However, the bar is crowded, and he doesn’t want to leave his full beer on the bar because he’s afraid someone will drink it. After a sudden burst of inspiration, he pulls out a small pad of paper and writes on it: “I spit in this beer.” Putting the note on the beer, he heads off to the bathroom. When he returns, he’s delighted to see his full beer still sitting there with the note. Upon closer examination, though, he sees that someone has written on the note: “So did I.”",
        "How do you know if someone likes craft beer? Don’t worry they’ll tell you.",
        "Stop trying to make everyone happy. You’re not beer.",
        "In heaven there is no beer, which is why we drink it here.",
        "If God had intended us to drink beer he would have given us stomachs.",
        "Beer. Because you can’t drink bacon.",
        "Beer is made from hops. Hops is a plant. Beer=salad.",
        "Spilling a beer is the adult equivalent of losing a balloon.",
        "To beer or not to beer, that is the question.",
        "You can’t find happiness at the bottom of a beer. Obviously, who is happy when their beer runs out?",
        "Life and beer are very similar. Chill for best results.",
        "Beer doesn’t have much vitamins, that’s why you have to drink lots of it."
    ]
    return random.choice(jokes)

if __name__ == '__main__':
    app.run()
