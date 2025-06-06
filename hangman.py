import re
from random import randint

# random list of 7-letter long words
words = ['Abalone', 'Abandon', 'Ability', 'Abolish', 'Abdomen', 'Abraham', 'Abyssal', 'Academy', 'Account', 'Achieve', 'Acidity', 'Acquire', 'Acrobat', 'Acronym', 'Acrylic', 'Actress', 'Adaptor', 'Address', 'Adjourn', 'Admiral', 'Advance', 'Advisor', 'Aerator', 'Aerosol', 'Affable', 'Afflict', 'Affront', 'African', 'Against', 'Ageless', 'Agendum', 'Agility', 'Agonize', 'Ailment', 'Airdrop', 'Airfare', 'Airflow', 'Airfoil', 'Airhead', 'Airlift', 'Airline', 'Airmail', 'Airplay', 'Airport ', 'Airship', 'Airshow', 'Airsick', 'Airtime', 'Airwave', 'Alamode', 'Alchemy', 'Alcohol', 'Alfalfa', 'Algebra', 'Alfredo', 'Alimony', 'Alkalic', 'Allergy', 'Almanac', 'Already', 'Alright', 'Alumnus', 'Alveoli', 'Amadeus', 'Amateur', 'Amazing', 'Ambient', 'Ambling', 'Amenity', 'America', 'Amiable', 'Ammonia', 'Amnesia', 'Amnesty', 'Amplify', 'Anagram', 'Analogy', 'Analyst', 'Analyze', 'Anarchy', 'Anatomy', 'Anchovy', 'Ancient', 'Android', 'Anemone', 'Angelic', 'Angrier', 'Angrily', 'Anguish', 'Angular', 'Animals', 'Animate', 'Annuity', 'Answers', 'Antacid', 'Antenna', 'Anthill', 'Anthrax', 'Antifog', 'Antique', 'Antonym', 'Anybody', 'Anymore', 'Anytime', 'Anxiety', 'Anxious', 'Apology', 'Apostle', 'Appease', 'Applaud', 'Appoint', 'Approve', 'Apricot', 'Aquatic', 'Aquifer', 'Archery', 'Archive', 'Archway', 'Arduous', 'Armband', 'Arousal', 'Arraign', 'Arrange', 'Arrival', 'Artists', 'Artwork', 'Ascetic', 'Ashtray', 'Asphalt', 'Aspirin', 'Assault', 'Astride', 'Atheist', 'Athlete', 'Attempt', 'Attract', 'Auction', 'Audible', 'Augment', 'Austria', 'Autopsy', 'Average', 'Aviator', 'Avocado', 'Awaking', 'Awesome', 'Awkward', 'Babysit', 'Backlit', 'Backlog', 'Backrub', 'Badland', 'Baggage', 'Bailout', 'Balance', 'Ballboy', 'Balloon', 'Baloney', 'Bananas', 'Bandage', 'Bandaid', 'Bangkok', 'Bargain', 'Bashful', 'Bastard', 'Battery', 'Beatles', 'Bedroom', 'Beehive', 'Believe', 'Beneath', 'Benefit', 'Berries', 'Between', 'Bicycle', 'Bifocal', 'Billion', 'Bipolar', 'Biscuit', 'Blocker', 'Blossom', 'Blowout', 'Bluejay', 'Blueray', 'Boycott', 'Bravery', 'Breaker', 'Brewery', 'British', 'Brownie', 'Browser ', 'Buffalo', 'Builder', 'Bulldog', 'Burgers', 'Burnout', 'Burrito', 'Cabinet', 'Calcium', 'Camelot', 'Campain', 'Capital', 'Capitol', 'Captain', 'Caption', 'Capture', 'Caravan', 'Carbarn', 'Cardoor', 'Careers', 'Careful', 'Caribou', 'Carkeys', 'Carrier', 'Cartoon', 'Cascade', 'Cassidy ', 'Catfish', 'Caution', 'Central', 'Century', 'Certain', 'Chalice', 'Chamber', 'Changes', 'Channel', 'Chapter', 'Charger', 'Charity', 'Charlie', 'Cheaper', 'Cheater', 'Checker', 'Checkup', 'Cheddar', 'Cheerio', 'Cheetah ', 'Cherish', 'Chicken', 'Chimney', 'Chipper', 'Choices', 'Choosey', 'Chopper', 'Chorale', 'Chowder', 'Circuit', 'Classes', 'Classic', 'Cleaner', 'Clinton', 'Closely', 'Clothes', 'Cockpit', 'Coconut', 'Coldest', 'Collage ', 'Collect', 'College', 'Colonel', 'Combine', 'Combust', 'Comedic', 'Comfort', 'Comical', 'Command', 'Commend', 'Comment', 'Commode', 'Commune', 'Commute', 'Compact', 'Company', 'Compare', 'Compass', 'Compete', 'Compile', 'Complex', 'Compose', 'Compute', 'Comrade', 'Concave', 'Conceal', 'Concede', 'Conceit', 'Concent', 'Concept', 'Concern', 'Concert', 'Concise', 'Concord', 'Condemn', 'Condone', 'Conduct', 'Conduit', 'Confess', 'Confide', 'Confine', 'Confirm', 'Conform', 'Confuse', 'Congeal', 'Conical', 'Conifer', 'Conjoin', 'Conjure', 'Connect', 'Conquer', 'Console', 'Consort', 'Consult', 'Consume', 'Contact', 'Contain', 'Contend', 'Content', 'Contest', 'Context', 'Contour', 'Control', 'Convent', 'Convict', 'Cookies', 'Correct', 'Corrupt', 'Costume', 'Cottage', 'Council', 'Counter', 'Country', 'Couples', 'Courage', 'Cowgirl', 'Cowhide', 'Cracker', 'Crapper', 'Crawler', 'Crazily', 'Creator', 'Crewcut', 'Crimson', 'Cripple', 'Crouton', 'Crucify', 'Cruelty', 'Cruiser', 'Crunchy', 'Crusade', 'Crybaby', 'Crystal', 'Cubicle', 'Cuisine', 'Culprit', 'Culture', 'Culvert', 'Cumulus', 'Cupcake', 'Cuplike', 'Curator', 'Curious', 'Current', 'Cursive', 'Curtail', 'Curtain', 'Cushion', 'Custard', 'Custody', 'Cutback', 'Cuticle', 'Cutlery', 'Cutlets', 'Cyclone', 'Cynical', 'Daycare', 'Daytime', 'Decades', 'Deceive', 'Declare', 'Decibel', 'Decimal', 'Declare', 'Decline', 'Decoder', 'Decorum', 'Default', 'Defence', 'Defiant', 'Deficit', 'Deflate', 'Defrost', 'Defuser', 'Degrade', 'Degrees', 'Delight', 'Deliver', 'Deltoid', 'Demerit', 'Denmark', 'Density', 'Dentist', 'Denture', 'Deplete', 'Deplore', 'Deposit', 'Depress', 'Deprive', 'Derrick', 'Dervish', 'Descent', 'Deserve', 'Desktop', 'Despair', 'Despite', 'Despond', 'Dessert', 'Destain', 'Destiny', 'Destroy', 'Detract', 'Develop', 'Devilry', 'Devious', 'Dewdrop', 'Diamond', 'Diapers', 'Diction', 'Diecast', 'Digital', 'Dignity', 'Disable', 'Disavow', 'Disband', 'Discard', 'Discern', 'Discord', 'Discuss', 'Disdain', 'Disease', 'Diseuse', 'Disgust', 'Disjoin', 'Dislike', 'Dismast', 'Dismiss', 'Disobey', 'Dispart', 'Display', 'Disport', 'Dispose', 'Dispute', 'Disrate', 'Disrobe', 'Disrupt', 'Disseat', 'Distort', 'Disturb', 'Dissect', 'Distant', 'Distend', 'Distich', 'Distill', 'Diverse', 'Divided', 'Divorce', 'Doctors', 'Dollars', 'Dolphin', 'Doorway', 'Dormant', 'Draught', 'Dreamer', 'Drivers', 'Dryness', 'Durable', 'Dynamic', 'Earache', 'Earlier', 'Earlobe', 'Eastern', 'Eclipse', 'Economy', 'Educate', 'Egotism', 'Elastic', 'Elderly', 'Elegant', 'Element', 'Elevate', 'Embassy', 'Embrace', 'Emotion', 'Empathy', 'Empress', 'Enclose', 'Endless', 'Enforce', 'English', 'Enhance', 'Enlight', 'Envious', 'Eternal', 'Ethical', 'Equinox', 'Equator', 'Evasive', 'Exactly', 'Example', 'Excited', 'Expense', 'Experts', 'Explain', 'Explode', 'Explore', 'Express', 'Extinct', 'Extract', 'Extreme', 'Eyebrow', 'Eyelash', 'Faceoff', 'Factoid', 'Factors', 'Faculty', 'Failure', 'Fanclub', 'Fantasy', 'Farmboy', 'Farmers', 'Fashion', 'Fastest', 'Fatigue ', 'Feature', 'Federal', 'Ferment', 'Ferried', 'Fiction', 'Fifteen', 'Fighter', 'Finally', 'Finance', 'Firedog', 'Firefly', 'Fireman', 'Fitness', 'Fixture', 'Flowers', 'Flulike', 'Flushot', 'Foolish', 'Footage', 'Forbear', 'Forearm', 'Foreign', 'Forever', 'Foreman', 'Forfeit', 'Forgive', 'Formula', 'Forsake', 'Fortune', 'Forward', 'Foxhole', 'Fragile', 'Frantic', 'Freezer', 'Freckle', 'Freedom', 'Freeway', 'Freight', 'Freshly', 'Friends', 'Frisbee', 'Fritter', 'Fumbled', 'Further', 'Gambler', 'Gameboy', 'Garages', 'Garbage', 'Gashose', 'Gastank', 'Gateway', 'General', 'Genesis', 'Generic', 'Genetic', 'Getaway', 'Giraffe', 'Glimpse', 'Glorify', 'Glucose', 'Goodbye', 'Gorilla', 'Governs', 'Gradual', 'Grammar', 'Grandma', 'Grandpa', 'Granite', 'Granola', 'Graphic', 'Gravity', 'Grocery', 'Habitat', 'Haircut', 'Halibut', 'Happily', 'Harbour', 'Harding', 'Harvest', 'Hatchet', 'Hateful', 'Healthy', 'Heights', 'Helpful', 'Heroism', 'Herself', 'Highest', 'Highway', 'Himself', 'History', 'Holiday', 'Holland', 'Homeboy ', 'Honesty', 'Hopeful', 'Hotcake', 'Hotdogs', 'Husband', 'Hydrant', 'Iceberg', 'Iceland', 'Icicles', 'Ideally', 'Idolize', 'Illicit', 'Illness', 'Imagine', 'Impound', 'Impress', 'Improve', 'Inboard', 'Inbound', 'Incense', 'Incisor', 'Incline', 'Inclose', 'Include', 'Incomes', 'Incubus', 'Indoors', 'Indulge', 'Infancy', 'Inferno', 'Infidel', 'Inflame', 'Inflate', 'Inflict', 'Ingrain', 'Ingrown', 'Inhaler', 'Inherit', 'Initial', 'Inkblot', 'Inkling', 'Inkwell', 'Inlayer', 'Inquire', 'Inquiry', 'Insects', 'Insider', 'Insight', 'Inspect', 'Inspire', 'Install', 'Instant', 'Instead', 'Instill', 'Insular', 'Insurer', 'Intense', 'Interim', 'Interns', 'Introit', 'Intrude', 'Intrust', 'Intwine', 'Invader', 'Invoice', 'Involve', 'Islamic', 'Islands', 'Isolate', 'Itemize', 'Jamaica', 'January', 'Jasmine', 'Jealous', 'Jewelry', 'Journey', 'Justice', 'Justify ', 'Kennedy', 'Keyhole', 'Keynote', 'Kingdom', 'Kinship ', 'Kitchen', 'Kittens', 'Kneecap  ', 'Lantern', 'Laundry', 'Lawsuit', 'Lawyers', 'Leaders', 'Learner', 'Leather', 'Lenscap ', 'Lessons', 'Letters', 'Liberal', 'Liberty', 'Library', 'License', 'Lincoln', 'Lipread ', 'Literal', 'Livable', 'Lobster', 'Logical', 'Lovable', 'Lovebug', 'Lullaby ', 'Machine', 'Madison', 'Madness', 'Magical', 'Magnify', 'Mailbag', 'Mailbox', 'Mailman', 'Majesty', 'Malaria', 'Maldive', 'Manager', 'Mandate', 'Manners', 'Markers', 'Married', 'Massage', 'Massive', 'Mastery', 'Meander', 'Measure', 'Medical', 'Members', 'Menthol', 'Mercury', 'Mermaid', 'Message', 'Methane', 'Michael', 'Midterm', 'Migrant', 'Migrate', 'Militia', 'Million', 'Misdial', 'Misfile', 'Mislead', 'Misread', 'Missile', 'Mission', 'Mistake', 'Mixture', 'Mobster', 'Modesty', 'Monarch', 'Monitor', 'Monolog', 'Monsoon', 'Monster', 'Montage', 'Monthly', 'Moocher', 'Moonlit', 'Morally', 'Morning', 'Moronic', 'Mortify', 'Mortise', 'Mudflap', 'Mudflow', 'Muffler', 'Muffins', 'Mundane', 'Musical', 'Mustang', 'Mustard', 'Mystery', 'Mystify', 'Nametag', 'Napkins', 'Narcism', 'Nations', 'Natives', 'Natural', 'Naughty', 'Nearest', 'Nebular', 'Necktie', 'Needles', 'Neglect', 'Nervous', 'Network', 'Neurons', 'Neutral', 'Neutron', 'Newborn', 'Newsboy', 'Niagera', 'Nickels', 'Nightly', 'Nirvana', 'Nitrate', 'Nocturn', 'Noisily', 'Nomadic', 'Nominal', 'Nonstop', 'Nostril', 'Notable', 'Notably', 'Nothing', 'Novelty', 'Noxious', 'Nuclear', 'Nucleus', 'Nudnick', 'Nullify', 'Numbers', 'Numeral', 'Nunlike', 'Nunnery', 'Nursery', 'Nurture', 'Nutcase', 'Obesity', 'Observe', 'Obvious', 'Octagon', 'Octopus', 'October', 'Offense ', 'Operate ', 'Opinion', 'Organic', 'Ottoman', 'Outback', 'Outcast', 'Outcome', 'Outdoor', 'Outrage', 'Outside', 'Overall', 'Package', 'Painful', 'Painter', 'Pajamas', 'Pandora', 'Panther', 'Paradox', 'Parents', 'Parties', 'Partner', 'Passion', 'Patient', 'Patriot', 'Payment', 'Peanuts', 'Penalty', 'Pennies', 'Pension', 'Percent', 'Perfect', 'Perform', 'Perfume', 'Persist', 'Phonics', 'Phrases', 'Physics', 'Picture', 'Pigears', 'Pigtail', 'Pilgrim', 'Pinball', 'Pintail ', 'Pioneer', 'Plastic', 'Playful', 'Plunder', 'Politic', 'Pollute', 'Popcorn', 'Poptart', 'Popular', 'Postage', 'Postbox', 'Postman', 'Praises', 'Prebake', 'Preboil', 'Precede', 'Precise', 'Predict', 'Preempt', 'Preface', 'Preheat', 'Preload', 'Prelude', 'Premade', 'Premier', 'Premise', 'Premium', 'Prepaid', 'Prepare', 'Preppie', 'Prequel', 'Presale', 'Present', 'Preshow', 'Presoak', 'Presume', 'Preteen', 'Pretend', 'Pretest', 'Pretzel', 'Prevail', 'Prevent', 'Preverb', 'Preview', 'Prewash', 'Preworn', 'Preying', 'Pricier', 'Prickly', 'Primage', 'Primary', 'Primate', 'Printer', 'Privacy', 'Private', 'Privies', 'Probate', 'Problem', 'Proceed', 'Process', 'Proctor', 'Procure', 'Prodigy', 'Produce', 'Product', 'Profane', 'Profess', 'Profile', 'Profuse', 'Progeny', 'Program', 'Project', 'Prolate', 'Proline', 'Prolong', 'Promise', 'Promote', 'Pronate', 'Pronoun', 'Propane', 'Prophet', 'Propose', 'Prorate', 'Prosody', 'Prosper', 'Protect', 'Protein', 'Protest', 'Protons', 'Proudly', 'Proverb', 'Provide', 'Provoke', 'Provost', 'Prowess', 'Prowler', 'Proxies', 'Prudent', 'Puberty', 'Publish', 'Pumpkin', 'Puppies', 'Purpose', 'Pursuit', 'Pyramid', 'Qualify', 'Quality', 'Quantum', 'Quarrel', 'Quarter', 'Queenly', 'Queerly', 'Quicken ', 'Quicker', 'Quickly', 'Quieter', 'Quietly', 'Quilter', 'Quinine', 'Quintet', 'Quitter', 'Raccoon', 'Racecar', 'Raceway', 'Radiant', 'Radical', 'Ragtime', 'Ragweed', 'Railcar', 'Rainbow', 'Rambler ', 'Rampant', 'Rampart', 'Rancher', 'Raisins', 'Ransack', 'Rapidly', 'Rapport', 'Rapture', 'Rattler ', 'Ravioli ', 'Reactor', 'Reality', 'Realize', 'Rebuild', 'Receipt', 'Receive', 'Recheck', 'Reclaim', 'Recline', 'Recover', 'Rectify', 'Recycle', 'Redbull', 'Redcoat', 'Redhead', 'Redline', 'Redneck', 'Redness', 'Redtail', 'Reducer', 'Redwood', 'Referee', 'Reflect', 'Refocus', 'Refract', 'Refrain', 'Refresh', 'Refugee', 'Refusal', 'Refutal', 'Regatta', 'Regimen', 'Regular', 'Reissue', 'Rejoice', 'Related', 'Relaxer', 'Relearn', 'Release', 'Remount', 'Reptile', 'Rescued', 'Rescuer', 'Reserve', 'Respect', 'Respond', 'Restate', 'Restore', 'Reteach', 'Retrain', 'Reunion', 'Reunite', 'Revolve', 'Ripcurl', 'Riptide', 'Riviera', 'Rosebud', 'Routine', 'Rowboat ', 'Rugrats', 'Sabbath', 'Sandman', 'Sarcasm', 'Satisfy', 'Scandal', 'Scenery', 'Scholar', 'Seabass', 'Seabird', 'Seafood', 'Seafowl', 'Seagull', 'Sealant ', 'Seaport', 'Seasick', 'Seaside', 'Seasons', 'Seawall', 'Seaward', 'Seaweed', 'Secrecy', 'Section', 'Secular', 'Secured', 'Serious', 'Selfish', 'Sellout', 'Sensors', 'Servant', 'Service', 'Setback', 'Settler', 'Seventy', 'Several', 'Shelter', 'Sheriff', 'Sherman', 'Shifter', 'Shirley', 'Shooter', 'Shorter', 'Sidearm', 'Sincere', 'Sitdown', 'Sixteen', 'Skijump', 'Skimask', 'Skipole', 'Skypark', 'Slavery', 'Smarter', 'Smuggle', 'Snowman', 'Snuggle', 'Society', 'Soldier', 'Someday', 'Speaker', 'Special', 'Species', 'Sponsor', 'Stadium', 'Stamina', 'Standup', 'Staples', 'Station', 'Storage', 'Stories', 'Stirfry', 'Stirrup', 'Streams', 'Strides', 'Student', 'Subject', 'Subsist', 'Subtext', 'Succeed', 'Success', 'Sucrose', 'Suggest', 'Suicide', 'Sulphur', 'Summary', 'Sunbath', 'Sunbelt', 'Sunbeam', 'Sunbelt', 'Sunburn', 'Sundays', 'Sundeck', 'Sundial', 'Sundown', 'Sunfish', 'Sunglow', 'Sunlamp', 'Sunland', 'Sunlike', 'Sunmaid', 'Sunrise', 'Sunroof', 'Sunroom', 'Sunsets', 'Sunspot', 'Support', 'Suppose', 'Supreme', 'Surgeon', 'Surgery', 'Survive', 'Suspend', 'Sweater', 'Swimmer', 'Swollen', 'Symptom', 'Tablets', 'Tabloid ', 'Tadpole', 'Talents', 'Tangent', 'Tangled', 'Taxcuts', 'Teacher', 'Teenage', 'Tension', 'Tequila', 'Termite', 'Terrify', 'Testify', 'Textile', 'Theatre', 'Therapy', 'Thermos', 'Thinker', 'Thirsty', 'Thought', 'Thunder', 'Timeout', 'Tubacco ', 'Toenail', 'Toering', 'Tonight', 'Tonnage', 'Topanga', 'Topdeck', 'Topless', 'Topload', 'Topples', 'Toprack', 'Topside', 'Topsoil', 'Tornado', 'Torture', 'Tourist', 'Towboat', 'Towhead', 'Tractor', 'Traitor', 'Transit', 'Treetop', 'Tribute', 'Trouble', 'Trouser', 'Trucker', 'Trumpet', 'Tuesday', 'Tunisia', 'Twinkle', 'Twister', 'Typhoid', 'Typical', 'Tyranny', 'Unhappy', 'Unheard', 'Unhinge', 'Unhitch', 'Unicorn', 'Unified', 'Uniform', 'Unitard', 'Unitary', 'Unkempt', 'Unknown', 'Unlatch ', 'Unlearn', 'Unleash', 'Unlevel', 'Unloose', 'Unlucky', 'Unquote', 'Unravel', 'Unready', 'Unscrew', 'Unstack', 'Unusual', 'Unwound', 'Unwoven', 'Updraft', 'Upfront', 'Upgrade', 'Upright', 'Upscale', 'Upstair', 'Upstate', 'Upsurge', 'Upswell', 'Upswept', 'Upswing', 'Uptight', 'Uranium', 'Urgency', 'Urinary', 'Urinate', 'Urology', 'Usually', 'Utensil', 'Utility', 'Utopian', 'Vacancy', 'Vaccine', 'Vagrant', 'Vaguely', 'Valance', 'Valuate', 'Valleys', 'Vampire', 'Vanilla', 'Vanload ', 'Vanpool', 'Variant', 'Variety', 'Vehicle', 'Velvety', 'Venison', 'Venture', 'Verdict', 'Version', 'Vibrate', 'Viceroy', 'Victory', 'Village', 'Vintage', 'Violate', 'Violent', 'Visitor ', 'Volcano', 'Waffles', 'Walnuts', 'Warbler', 'Warfare', 'Warrior', 'Washers', 'Wealthy', 'Weather', 'Webcast', 'Website', 'Webster', 'Weekend', 'Welcome', 'Welfare', 'Western', 'Wetness', 'Wetsuit', 'Whoever', 'Windows', 'Winners', 'Wipeout', 'Wiseman', 'Without', 'Witness', 'Worldly', 'Worship', 'Wrestle', 'Wronged', 'Zealous']

# use randint to populate index number -- rand int is an inclusive range
word = words[randint(0, len(words)-1)].upper()

# initialize variables
guessed_letters = []
win = False
fail_count = 0
prev_turn_message = ''
display_word = "_ " * len(word)
available_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_guess():
    try:
        guess = input("Guess a letter: ")
        if len(guess) != 1 or re.search(r'\d', guess):
            print('Please enter a single letter.')
            raise ValueError
    except ValueError:
        return get_guess()
        '''
            the result of the get_guess function call must be returned.
            If it's not returned the guessed letter can cause fail_count to increment
            and the player can also guess the same letter and be dinged for it twice
            I opted to return it as opposed to reassigning guess value.
        '''
    return guess


def display_hangman(fail_count, win=False):
    # The backslash, \, is an exit(escape) character, and also needs to be exited. To print \ the string must look like '\\'
    # multi-line formatted string, code in brackets will be interpolated
    return f'''
        -----
        |   |
        |   {'O' if fail_count > 0 else ''}
        |  {'/|' if fail_count == 3 else ''}{' |' if fail_count == 2 else ''}{'/|\\' if fail_count >= 4 else ''}
        |   {'|' if fail_count > 1 else ''}
        |  {'/' if fail_count == 5 else ''}{'/ \\' if fail_count == 6 else ''}
    ----------
{'Sorry, you lost.\nJeff died.' if fail_count > 5 else ''}{"You saved a murderer from certain death.\nI hope you're happy!" if win else ''}
    '''
def play_hangman(words):
    word = words[randint(0, len(words)-1)].upper()

    # initialize variables
    guessed_letters = []
    win = False
    fail_count = 0
    prev_turn_message = ''
    display_word = "_ " * len(word)
    available_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Game starts 
    while fail_count != 6 and not win: 
        # Show the word progress 
        # The underscore or the letter to show the progress of how many has been guessed 
        print(display_hangman(fail_count))
        if not win:
            print(prev_turn_message) # print error message
        prev_turn_message = '' # reset error message
        print(" ".join(display_word), '\n')
        
        print(" ".join([letter for letter in available_letters if letter not in guessed_letters]))
        
        guess = get_guess().upper()

        # Add it to our guessed letters 
        if guess in guessed_letters:
            prev_turn_message = f"You already guessed this letter: {guess}"
        else:
            guessed_letters.append(guess)
            if guess in word:
                count = word.count(guess)
                prev_turn_message = f"Correct! {guess} is in the word exactly {count} time{'s' if count > 1 else ''}"
                display_word = " ".join(map(lambda ch: ch if ch in guessed_letters else "_", word))
                win = '_' not in display_word
                
            else:
                fail_count += 1
        print('\n--------------------------------------------------\n')
                
    print(display_hangman(fail_count, win))
    
if __name__ == '__main__':    
    play_hangman(words)

    again = input("Play again? (y/n): ").lower()
    if again in ('y', 'yes'):
        play_hangman(words)
    else:
        exit
