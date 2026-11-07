"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "Space typically would not be considered a symbol, but in his Prehistory: The Making of the Human Mind, Colin Renfrew defined a symbol as “X (the symbol, or signifier) represent[ing] Y (the thing signified) in context C” (Renfrew 93). In this definition, the people of Uruk used space as a symbol, representing power and religion. However, spatial organization is not the only symbol in the image. Renfrew also designated words, thoughts, and material things as symbols (Renfrew 91-92). These are present within the image as well, and play off of spatial distribution to emphasize religion and power in Uruk.",
            "Another similarity between the two religions seems to be the concept of judgment. In the final scenes of The Baal Cycle, Death is threatened with having his “scepter of judgment” destroyed, implying that Death had some form of judgment over those who died (The Baal Cycle 191). Likewise, the Book of the Dead states that the concept of an Egyptian afterlife relies on a final “judgment” in front of Osiris and a council of gods (Lichtheim 443). A judgment after death appears in both religions and cultures, meaning both understood morality and had a clear idea of right and wrong.",
            "Language loss, a global phenomenon, is accelerating among indigenous groups in the United States. A large majority of Native American vernaculars are spoken only by elders and the remainder are fast approaching that status, as growing numbers of children speak only English. Inevitably comparisons are drawn between the threat to language diversity and the (better-publicized) threat to biological diversity. Yet biomorphic metaphor—e.g. ""language murder," "language suicide""—can be simplistic and misleading. They tend to distort answers to critical questions in formulating a policy response: What causes language loss? How can it be reversed? Why should we care?",
            "The now-contemplated field of Data Science amounts to a superset of the fields of statistics and machine learning which adds some technology for ‘scaling up’ to ‘big data’. This chosen superset is motivated by commercial rather than intellectual developments. Choosing in this way is likely to miss out on the really important intellectual event of the next fifty years.",
            "Some theories of strike activity suggest that the settlement probability of a strike depends on the number of workers involved in the strike. Additionally, much recent em- pirical research on strikes has been constrained by data availability to look only at strikes in large bargaining units. It is natural to ask, therefore, whether strike size systematically influences strike duration, and whether this question poses problems of interpretation for studies confined to samples of large strikes. This paper uses Canadian strike data to ex- amine these questions. We find that size is an important determinant of strike duration and also that studies of strike duration based only on large strikes can yield results that are not representative of the influences for all strikes.",
            "At the end of World War II, the world had once again experienced a change in the world order. Many Western nations relied on their empires and colonies to sustain them through the war; the colonies fought along\side Western soldiers and supported them behind the front lines with supplies and the necessary infrastructure. As the war ended, many colonies experienced a shift towards nationalist thinking, as a result of a combination of promises made to colonies by European powers, demands for equal compensation by colonial war veterans, a rise in an educated colonial class, and the overall weakening of European powers. Over the course of the next 30 or so years after the end of World War II, many former colonies would successfully become independent nations. Despite gaining their independence, former colonies turned nations would still not be free of the influence of Western nations and former imperial powers, who exerted their power over newly independent nations by means of environmental impact, military action, and trade relations, all of which produce economic impacts and instability on the nations that were once imperial colonies.",
            "My argument depends not on immutable essences of species as such but on received meanings of wildness for any animal at all. The modern zoo promises its visitors a brush with the wild, and the premium of this entertainment value is evident in the current effort increasingly to display animals in mock- ups of their natural habitats. However, sheer placement in a recreated habi- tat cannot provide the experience that zoo visitors seek. ",
            "Stars, not unlike a shriveling fruit left out in the sun for too long, will shrink in size over the course of their lifetime. They will also lose mass in the form of stellar wind, similar to how a sunbaked fruit loses mass in the form of water evaporation. However, unlike an unfortunate peach sitting in the sun (or apricot or plum or some other form of stone fruit or tomato), stars also expand in size at some point in their stellar life. It is here that this fruit-star metaphor starts to break down. The manner in which a star loses its mass has obvious connections to its stellar evolution. Starting from the protostar stage and ending in some form of stellar death, stellar wind and mass loss are present at every moment.",
            "Early projections show Democrats winning both chambers of Congress. NBC says they flipped seven Senate seats and have reached a House majority with at least 218 seats, though dozens of House races and some AP calls were still pending as of Nov 4–6. Hakeem Jeffries is in line to become Speaker, which means divided government for the last two years of Trump's second term.",
            "People often call oat milk a health food, but most commercial versions are low in protein. Many also contain added oils and sugars, which form during processing when enzymes break oat starch into maltose. And ""plant-based"" doesn't automatically mean more nutritious or less processed than dairy milk or other alternatives, even though oat milk does have a fairly low environmental footprint."
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "People often call oat milk a health food, but most commercial versions are low in protein. Many also contain added oils and sugars, which form during processing when enzymes break oat starch into maltose. And ""plant-based"" doesn't automatically mean more nutritious or less processed than dairy milk or other alternatives, even though oat milk does have a fairly low environmental footprint.",
            "Another similarity between the two religions seems to be the concept of judgment. In the final scenes of The Baal Cycle, Death is threatened with having his “scepter of judgment” destroyed, implying that Death had some form of judgment over those who died (The Baal Cycle 191). Likewise, the Book of the Dead states that the concept of an Egyptian afterlife relies on a final “judgment” in front of Osiris and a council of gods (Lichtheim 443). A judgment after death appears in both religions and cultures, meaning both understood morality and had a clear idea of right and wrong.",
            "Early projections of the recent midterm elections show Democrats winning both chambers of Congress. According to NBC, they have flipped seven Senate seats and 40 House seats. Regardless, many House races still remain in play and have yet to be called. Hakeen Jeffries is set to be the next Speaker of the House, and the Democrat's control of Congress means divided government for the last two years of Trump's second presidential term. ",
        ],
    },

    {
        "name": "unsure text is labeled as such",
        "criterion": 4,
        "texts": [
            "Early projections of the recent midterm elections show Democrats winning both chambers of Congress. According to NBC, they have flipped seven Senate seats and 40 House seats. Regardless, many House races still remain in play and have yet to be called. Hakeen Jeffries is set to be the next Speaker of the House, and the Democrat's control of Congress means divided government for the last two years of Trump's second presidential term. ",
            "Bees are flying insects belonging to the clade Anthophila, known worldwide for their vital role as plant pollinators. There are over 20,000 known species of bees globally, with about 4,000 species native to North America. Bees feed exclusively on flower nectar (for energy) and pollen (for protein). While well-known species like the western honey bee (Apis mellifera) live in large, organized hives with a queen, workers, and drones, the vast majority of bee species are solitary and nest in the ground or in hollow plant stems.",
            "Oat milk often gets called a health food, but in reality it tends to be low in protein and many contain added oils. Sugars are also formed during processing when enzymes break the starch into maltose. ""Plant-based"" also doesn't mean more nutritious or less processed than regular dairy milk, even if oat milk has a fairly low environmental footprint."
            ]
    } 
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
