"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask,jsonify,request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


data =[
    {
	"Islamic Daawah":"All the prophets of God including; Adam, Noah, Abraham, Issac, Jacob, and the tribes, Jesus, and Muhammad (peace be upon them), invited the people to the same thing, to worship The One God without any partners, son or associates.",
	"Fastest Growing Religion":"Islam: The fastest growing religion in the world, specifically, the fastest growing religion amongst women and young people.",
	"Tawheed":"Linguistically the word tawheed means unification (to make something one). However Islamically it is in reference to Allaah being singled out alone, in all that is particular to him.",
	"Shirk":"The opposite of tawheed is 'Shirk' which is to associate partners with Allaah by giving that which belongs to him, to others.",
	"Religion of Abraham":" Islam is the true religion of Abraham, because Abraham completely submitted himself to the revealed will of Almighty God.",
	"Eternal Message":"The Pure Monotheism of Islam, as well as its universal brotherhood/sisterhood, strong morals and positive outlook on life, is still very relevant and meaningful to modern societies. The continued relevance and applicability to both the spiritual and worldly life of human beings from all around the word is just one of the many proofs of the Divine origin of the message of Islam.",
	"Moderation":"The teachings of Islam, since they are divinely revealed, are balanced in all of their aspects. Even though Islam is an all-encompassing way of life, it preaches moderation and rejects extremism. On the one hand, Islam does not preach complete rejection of all worldly pleasures in view of the life hereafter; and on the other hand it does not teach that earthly life is just for pleasure and enjoyment. In Islam, wealth and worldly pleasures can be partaken of in this life as long as they are enjoyed in a way that is in obedience to God. However, Muslims are taught to keep in mind that the life hereafter is their ultimate goal, and therefore one should be charitable and not become too attached to worldly things. By maintaining a balance between man's spiritual and physical needs, the teachings of Islam are best suited for the needs of human beings in particular and society in general.",
	"Prophet Muhammad":"The Prophet Muhammad's mission encompassed not only spiritual and religious teachings, but also included guidance for such things as social reform, economics, politics, warfare and family life. Thus due to the diversity and success of Muhammad's mission, Muslims have clear guidance from God and His Final Prophet on all aspects of life.",
	"Universal Message":"The pure essence of the beliefs and teachings that were revealed by God to the Prophet Muhammad are the same as God taught to Abraham, who was one of the earliest and greatest prophets. So actually, Muhammad is the final prophet of Islam -- not the first. Additionally, Islam is the true religion of Abraham, because Abraham completely submitted himself to the revealed will of Almighty God.",
	"Worship":"Almighty God has revealed in the Noble Qur'an that His purpose for creating human beings was to worship Him and Him alone. Like other religions, Islam has required acts of worship, however worship in Islam is not limited to rituals. Since Islam is an all-encompassing religion with guidance for all aspects of life, almost every action in a Muslim's life becomes an act of worship if it is done to build a better relationship with God. Since man's purpose in life is to worship and submit to God, worship in Islam has been defined by God Himself in an all-encompassing way.",
	"God":" the concept of God in Islam is completely based upon Divine Revelation. Not only is the concept of God in Islam characterized by purity and clarity, but it is also not marred by myths, superstitions or man-made philosophical ideas. In the pure and straightforward teachings of Islam, Almighty God has clearly revealed His unique nature and qualities to man in the way which He wants them to be understood. ",
	"Muhammad":"He proved himself to be ideal of manhood, and to possess a spotless character. He was the most obliging to his compatriots, honest in his talk and mildest in temper. He was gentle-hearted, chaste, hospitable and always impressed people by his piety inspiring countenance. He was always truthful and the best to keep covenant. His fellow citizens by common consent gave him the title of Al Ameen (trustworthy).",
	"Jesus said":"And (remember) when Jesus, son of Mary, said: O Children of Israel! I am the Messenger of Allaah unto you, confirming the Torah (which came) before me, and giving glad tidings of a Messenger to come after me, whose name shall be Ahmad. But when he (Ahmad i.e. Muhammad) came to them with clear proofs, they said: This is plain magic.",
	"Prophets of God":"Verily, We have inspired you (O Muhammad) as We inspired Noah and the Prophets after him; We (also) inspired Abraham, Ishmael, Isaac, Jacob, and Al-Asbat, (the twelve sons of Jacob), Jesus, Job, Jonah, Aaron, and Solomon, and to David We gave the Psalms. And Messengers We have mentioned to you before, and Messengers We have not mentioned to you, and to Moses, Allah spoke directly.",
	"Muhammad not father":"Muhammad is not the father of any man among you, but (he is) the Messenger of Allaah, and the Last of the Prophets, And Allaah is Ever All-Aware of Everything",
}
]


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/islaam/data',methods=['GET'])
def getAll():
    return jsonify(data)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
