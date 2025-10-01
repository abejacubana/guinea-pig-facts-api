from flask import Flask
import random

app = Flask(__name__)

facts = [
    "Guinea pigs have four toes on their front feet and three on the back.",
    "Their teeth never stop growing—up to 3 mm per week.",
    "They can jump (popcorn) when excited, often mid-sprint.",
    "Guinea pigs are born fully furred with open eyes and teeth.",
    "They can recognize their owners by voice and scent.",
    "A group of guinea pigs is called a 'herd.'",
    "They communicate with over 10 distinct vocalizations.",
    "Guinea pigs can sleep with their eyes open.",
    "They don’t produce vitamin C naturally—just like humans.",
    "Their scientific name is Cavia porcellus.",
    "Guinea pigs have a 330-degree field of vision.",
    "They can’t sweat or pant—heatstroke is a real risk.",
    "Their teeth form a perfect occlusion when healthy.",
    "They purr when content, but also when mildly annoyed.",
    "Males are called boars, females are sows.",
    "They can live 5–8 years, sometimes longer with care.",
    "Guinea pigs have a 'barbering' behavior—chewing others’ fur.",
    "They’re crepuscular—most active at dawn and dusk.",
    "Their hearing range is wider than humans.",
    "They can learn simple tricks with repetition and treats.",
    "Guinea pigs have no tail—just a vestigial bump.",
    "They’re illegal to own in some places like California classrooms.",
    "They can jump up to 12 inches vertically.",
    "Guinea pigs have 20 teeth—no molars.",
    "They produce two types of poop—one they eat for nutrients.",
    "They can distinguish between individual humans.",
    "Guinea pigs were domesticated over 3,000 years ago.",
    "They’re native to the Andes Mountains.",
    "They’re used in scientific research due to their physiology.",
    "Guinea pigs can get bored—enrichment is essential.",
    "They have a strong hierarchy when housed together.",
    "Guinea pigs can run up to 6 mph in short bursts.",
    "They can be litter trained with consistency.",
    "Their nails grow continuously and need trimming.",
    "Guinea pigs can suffer from scurvy without vitamin C.",
    "They love hiding—tunnels and huts reduce stress.",
    "They have a 'freeze' response to sudden sounds.",
    "Guinea pigs can emit a high-pitched 'wheek' for food.",
    "They groom themselves frequently—very clean animals.",
    "Guinea pigs can bond deeply with cage mates.",
    "They have sensitive whiskers for spatial awareness.",
    "Guinea pigs can get fungal infections from damp bedding.",
    "They mark territory with scent glands near their rear.",
    "Guinea pigs can be allergic to pine and cedar bedding.",
    "They can eat hay nonstop—it helps wear down teeth.",
    "Guinea pigs can get lonely—companionship is key.",
    "They can climb low ramps but not steep ones.",
    "Guinea pigs have a unique digestive system called hindgut fermentation.",
    "They can get 'zoomies' when overstimulated.",
    "Guinea pigs can chirp like birds—rare and mysterious."
]

@app.route("/")
def random_fact():
    return random.choice(facts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
