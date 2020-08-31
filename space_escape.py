import random
from sys import exit

class Scene:

    def enter(self):
        pass

class Engine:

    def __init__(self, scene_map):
        self.mapper = scene_map                                                 # set an attribute of the Engine, to be a 'map' object

    def play(self, human_being):
        self.mapper.opening_scene()                                             # opening text
        self.mapper.crt_scene.enter()                                           # corridor description

        act_1 = input("What will you do? Search for a weapon / investigate what you see ahead? ")
        if "weapon" in act_1 or "Weapon" in act_1 or "search" in act_1 or "Search" in act_1:                           # if "weapon" or "search" or "Search" in act_1: does NOT work
            likelihood = random.randint(1,10)
            if likelihood < 3:
                print("\tYou look around. There are no weapons to be seen! Welp - looks like you are on your own. It's time to investigate.")
            elif likelihood in range(3,9):                                      # 3->8
                print("\tYou look around. There - to one side, under a bag, you see a baton and pick it up! It's time to investigate.")
                human_being.weapon_possessed = 'baton'
            elif likelihood in range(9,11):
                print("\tYou look around. No way! Over there - a rare ConfuseRay gun! You pick it up immediately - it's time to investigate.")
                human_being.weapon_possessed = 'ConfuseRay'
            else:

                self.mapper.next_scene(Death('\tSomething went wrong when finding the weapon :('))                                                 # !!!!!!!!!!!!!!!!!!!!!!!!!!!
                self.mapper.crt_scene.enter()

        elif "investigate" in act_1 or "Investigate" in act_1:
            pass
        else:

            self.mapper.next_scene(Death('\tNext time, choose one of the two options!'))
            self.mapper.crt_scene.enter()

        print("\tYou walk up to the unidentified being in front of you. As suspected, it is some kind of alien.")
        act_2 = input("What will you do now? Fight? Or speak? ")
        if "fight" in act_2 or "Fight" in act_2:
            print("""\
        As you tower over the alien - a strange vibration begins to fill the corridor. Just then - bang!
        A huge flash of light! You instinctively shield your eyes. Once the warmth on your eyelids begins to wane,
        you slowly open them. In front of you stands a six-armed beast. It is pretty clear that you can't win this fight.
        The beast grabs your arm and begins to twist. \"Apologise now!\" it snarls.""")

            act_3 = input("Do you apologise? ")
            acceptables = ['sorry', "Sorry", 'apologise', "Apologise", 'yes', "Yes"]

            if 'sorry' in act_3 or 'Sorry' in act_3 or 'apologise' in act_3 or 'Apologise' in act_3 or 'yes' in act_3 or 'Yes' in act_3:
                print("\tThe alien gladly lets you go. \'Apology accepted - I hate to fight\' says the alien. I suppose you are wondering who I am.")

            else:

                self.mapper.next_scene(Death('\tPride comes before a fall...'))
                self.mapper.crt_scene.enter()

        elif 'speak' in act_2 or 'Speak' in act_2 or 'talk' in act_2 or "Talk" in act_2:
            pass
        else:

            self.mapper.next_scene(Death('\tNext time, choose one of the two options!'))
            self.mapper.crt_scene.enter()

        print("""\
        My name is 74-101-102-102. In your language, my name is Jeff.
        While it is true that my people seek to conquer, I seek a higher
        power...fun! You see, before I was drafted for this fight, I was a
        comedian. I love jokes, but unfortunately my people don't seem to share
        my passion. Since we have already obtained what we came for, I will
        grant you safe passage if you can make me laugh. So go on, tell me a
        joke - I only care for one-liners!\" """)

        act_4 = input("What do you say? Remember - it likes one-liners! ")
        outcome = random.randint(1,5)
        if outcome >= 2:
            print("""\
        The alien is silent. You begin to back away. \"HAHAHAHA\" - the
        alien has burst out laughing. This is your chance to get away.""")

        elif outcome == 1:
            print("\tThe alien is silent. You begin to back away.")

            self.mapper.next_scene(Death('\tAs for comedy - don\'t quit your day job...'))
            self.mapper.crt_scene.enter()

        else:

            self.mapper.next_scene(Death('\tSomething went wrong when the alien was judging the joke.'))
            self.mapper.crt_scene.enter()

        counter = 0

        while counter < 10:
            act_5 = input("Where now? The Armory or the Bridge? ")

            if "left" in act_5 or "Left" in act_5 or "armory" in act_5 or "Armory" in act_5:
                counter = 10
                self.mapper.next_scene(LaserWeaponArmory())                     # You can do this, and change the field of the Map because you have the object reference, not just a copy. [mutability?]

            elif "right" in act_5 or "Right" in act_5 or "Bridge" in act_5 or "bridge" in act_5:
                counter = 10
                self.mapper.next_scene(TheBridge())

            else:
                counter +=1
                if counter == 9:
                    print("\tThe alien has stopped laughing and is tired of your poor decisions.")

                    self.mapper.next_scene(Death('\tNext time - pick one of the options!'))
                    self.mapper.crt_scene.enter()

                elif counter < 9:
                    pass

                else:

                    self.mapper.next_scene(Death('\tSomething strange happened as you were deciding where to go.'))
                    self.mapper.crt_scene.enter()

        self.mapper.crt_scene.enter()                                           # Print description of current scene.
        if isinstance(self.mapper.crt_scene, LaserWeaponArmory):                # A way to check if an object is an instance of a certain class (includes inheritance)
            print("""\
        You walk up to the vault door. Out of the corner of your eye,
        you notice a manifest for the vault. Scanning through the list, you
        see lots of huge weapons. However there are two that could fit into
        your bag. A neutron bomb or an ion blaster. The bag is only large
        enough for one item - anyway, you are getting ahead of yourself.
        Gingerly, you push the alien body aside and stare at the keypad on
        the door. You'll have to crack this before you can access the
        weapons. It appears to be a 4-digit code.""")

            code = random.randint(0,9999)
            code_str = str(code)
            code_list = list(code_str)
            while len(code_list) < 4:
                code_list.insert(0,'0')                                         # leading 0s

            code_3_dig_str = ''.join(code_list[0:3])
            code_4_dig_str = ''.join(code_list)

            act_6 = input("Guess the code or search for clues? ")
            if 'search' in act_6 or 'Search' in act_6:

                print("""\
        You search around alien for clues. Just as you are about to give
        up, you see something on the alien's reader. There is a message,
        'The code is: """, end = '')
                print(code_3_dig_str,'_','\'',sep = '')
                print("\tIt appears that the last digit of the code is missing")
            elif 'guess' in act_6 or 'Guess' in act_6:
                pass
            else:

                self.mapper.next_scene(Death('\tNext time - pick one of the options!'))
                self.mapper.crt_scene.enter()

            iterator = 7
            while iterator >= 1:
                prompt_string = "Enter the code now. You have " + str(iterator) + " tries remaining: "
                act_7 = input(prompt_string)
                if act_7 == code_4_dig_str:
                    print("\tThe door whines as it shudders open - you got it!")
                    break
                else:
                    print("\tNo dice - that didn't work")
                    iterator -= 1
            else:
                print("\t'Bang!' The door behind you opens. Looks like you are out of time")

                self.mapper.next_scene(Death('\tKeep trying - there is more chance involved than you might think! Try to get as much information as possible before attempting the code.'))
                self.mapper.crt_scene.enter()

            print("""\
        The shelves in front of you are lined with weapons. Among them, you see
        the ion blaster and one neutron bomb. 'That's odd' you think to yourself.
        'I could have sworn we had more bombs...'""")
            act_8 = input("Which do you take? ")

            list_of_answers_1 = ['neutron','Neutron','bomb','Bomb']
            list_of_answers_2 = ['ion','Ion','blaster','Blaster']

            if 'neutron' in act_8 or 'Neutron' in act_8 or 'bomb' in act_8 or 'Bomb' in act_8:
                print("\tYou put the weapon in your bag and head to the Bridge")
                human_being.bomb_possessed = True
                self.mapper.next_scene(TheBridge())
                self.mapper.crt_scene.enter()

            elif 'ion' in act_8 or 'Ion' in act_8 or 'blaster' in act_8 or 'Blaster' in act_8:
                print("You put the weapon in your bag and head to the Bridge")
                self.mapper.next_scene(TheBridge())
                self.mapper.crt_scene.enter()
            else:
                print("That didn't work. You head to the Bridge.")
                self.mapper.next_scene(TheBridge())
                self.mapper.crt_scene.enter()
                                                                                # in bridge
        print("""\
        Time is running out.""")
        act_secret = input("What do you do? ")
        if "search" in act_secret or "Search" in act_secret:
            print("""\
        As you rummage through the mess on the floor at your feet - you
        notice a reader on one of the alien's arms. There is a diagram with
        two sets of five circles. Four have been crossed out. Though this is
        strange, you commit it to memory.""")

            human_being.diagram = True
        else:
            pass

        print("""\
        In desperation, you head for the alien on the bridge. As you get closer,
        you realise the alien looks like a human. You both are around the same
        height and the alien has a wiry frame. Only, muscular tentacles radiate
        from the alien's abdomen. "Out of my way!" you exclaim. You know that
        this alien is the only thing between you and freedom. The tentacles
        suddenly align towards you. The alien snarls. Looks like you have a
        fight on your hands.""")

        act_9 = input("Will you fight? ")
        if "yes" in act_9 or "Yes" in act_9 or 'fight' in act_9 or "Fight" in act_9:
            outcome_determined = random.randint(1,10)
            if human_being.weapon_possessed == None:
                if outcome_determined >= 9:
                    print("""\
        Despite your lack of weapons, you best the alien in hand
        to...er...tentacle combat. You head through to the pod room.""")
                    self.mapper.next_scene(EscapePod())

                else:
                    print("\tThe alien knots your hands together with tentacles. Oh dear.")

                    self.mapper.next_scene(Death('\tOh dear. A good weapon might help with this - where might you find one?'))
                    self.mapper.crt_scene.enter()

            elif human_being.weapon_possessed == 'baton':
                if outcome_determined >= 5:
                    print("""\
        With the baton you fight the alien off. Good work. You
        head to the pod room.""")
                    self.mapper.next_scene(EscapePod())
                else:
                    print("\tThe alien seizes the baton from you. How the turn tables.")

                    self.mapper.next_scene(Death('\tOh dear. A better weapon might help you - keep trying!'))
                    self.mapper.crt_scene.enter()

            elif human_being.weapon_possessed == 'ConfuseRay':
                if outcome_determined >= 2:
                    print("""\
        You zap the alien with the ConfuseRay. The alien is confused!
        It hurt itself in its confusion! Incapacitated, the alien
        is no longer a barrier. You head to the pod room.""")
                    self.mapper.next_scene(EscapePod())
                else:
                    print("""\
        You zap the alien with the ConfuseRay. The alien is confused!
        The alien snapped out of confusion! Uh-oh...""")

                    self.mapper.next_scene(Death('\tOh dear. Keep trying! Sometimes even the best laid plans go awry.'))
                    self.mapper.crt_scene.enter()
            else:

                self.mapper.next_scene(Death('\tSomething went wrong when determining your weapon.'))
                self.mapper.crt_scene.enter()
        else:                                                                   #if you don't fight
            print("\tUnfortunately this alien doesn't share his colleague's sense of humour.")

            self.mapper.next_scene(Death('\tSometimes you need to fight!'))
            self.mapper.crt_scene.enter()

        if human_being.bomb_possessed == True:
            print("\tBefore you go, you arm the bomb. Best not to forget that!")

        self.mapper.crt_scene.enter()                                           # In the pod room.
        continuing = input('Press any key to continue: ')
        print("""\
        Surveying the room once more, you realise that you will have to
        eliminate some of your options quickly to find a viable pod. There are
        ten pods in total, five to your left and five to your right. Five of the
        pods are gone - used by the rest of your team. That leaves five from
        which to choose. Two of them clearly have been rigged to explode - the
        trail of explosives out is a dead giveaway. OK - three left. You hear
        the aliens checking on their buddies at the Bridge. There is no time -
        you have to choose a pod!""")
        capsules = [*range(1,11)]

        pod_c_1 = random.choice(capsules)
        capsules.remove(pod_c_1)

        pod_c_2 = random.choice(capsules)
        capsules.remove(pod_c_2)

        pod_c_3 = random.choice(capsules)
        capsules.remove(pod_c_3)

        pods = [pod_c_1, pod_c_2, pod_c_3]
        real_pod = random.choice(pods)
        print("\tThe pods left are numbers: ", end = '')
        for i in pods:
            print(i,', ',sep = '', end = '')

        continuing = input("\nPress any key to continue: ")

        if human_being.diagram == True:
            print("""\
        \tJust before you choose a pod - you remember the diagram with circles!
        Could it be...? Yes, those two that have been rigged - they match two
        of the four crossed-out pods! And the five that your crew escaped in have
        not been marked. The aliens couldn't bomb empty escape pods! This means
        that you can eliminate two more of the pods. Those that have been crossed
        have been rigged, so that leaves only one pod!""")
            print("\tYou realise that the only safe pod is number:", real_pod)
        else:
            pass

        final_act = input("Which pod do you choose? ")
        if int(final_act) == real_pod:
            if human_being.bomb_possessed == True:
                print("""\
        You get in the pod and press eject. Closing your eyes, you
        mutter a quick prayer. You can just hear the clamor of the aliens
        entering the pod room as the bomb explodes and you are jettisoned
        from the craft.
        ....
        \'Took you long enough T1'\ says a familiar voice.
        YOU WIN.""")
            else:
                print("""\
        You get in the pod and press eject. Closing your eyes, your
        mutter a quick prayer. You can just hear the clamor of the aliens
        entering the pod room. Nothing's happening. You look up and your
        stomach turns. The aliens must have disabled the 'eject' buttons
        after your team left! As the aliens open your pod and yank you
        out, your friend's initial instructions echo through your mind.""")

                self.mapper.next_scene(Death('\tTry again - pay attention to the instructions!'))
                self.mapper.crt_scene.enter()
        else:
            self.mapper.next_scene(Death('\tSomething went wrong. Careful as you choose the pods. Search EVERYWHERE!!'))
            self.mapper.crt_scene.enter()


class Death(Scene):                                                             # death description

    def __init__(self,exit_str):
        self.err_msg = exit_str

    def enter(self):
        print("""\
        You open your eyes...is this...heaven?
        You look around. Who is that? Is that...God?
        GAME OVER.""")
        exit(self.err_msg)

class CentralCorridor(Scene):                                                   # corridor description

    def enter(self):
        print("""\
        You are in the central corridor. To your left, the Armory. To your right, the Bridge.
        But directly ahead of you - something that looks like an alien!""")

class LaserWeaponArmory(Scene):                                                 # Armory description

    def enter(self):
        print("""\
        You enter the Armory and look around. Lights are flickering and live
        cables are sparking on the floor, writhing like snakes. A foul smell
        fills the air as your gaze reaches the body of an alien guard, slumped
        at the foot of the Vault Door.""")

class TheBridge(Scene):                                                         # Bridge description

    def enter(self):
        print("""\
        Your footsteps begin to echo as you reach the bridge. In front of you
        is a vast cavern, previously used for large-scale experiments. All the
        equipment now lies at the bottom, since the aliens turned on their
        Gravity Engine. Just in fron of you lie two aliens - knocked out.
        Up ahead: a reinforced steel bridge that is now the only method of safe
        passage to the escape pods. But wait! Is that...another alien?""")

class EscapePod(Scene):

    def enter(self):                                                            # EscapePod description
        print("""\
        You duck as you enter a dingy cavern. This is the escape-pod room -
        your ticket to freedom. As you look around, you see the remnants of
        explosives littered around the room. You go closer to inspect. Bombs!
        The aliens were making bombs and have likely planted them in some of
        the pods. You can hear the remaining aliens making their way across the
        bridge. Time is running out!""")

class Human():                                                                    #this is mainly to store information about the player's state.
    def __init__(self,bomb_state,weapon,paper):
        self.bomb_possessed = bomb_state
        self.weapon_possessed = weapon
        self.diagram = paper
class Map:

    def __init__(self, start_scene):
        if 'central_corridor' in start_scene:                                   #checking we start in corridor
            self.crt_scene = CentralCorridor()                                  #create an object of type CentralCorridor and store in the current_scene field.
            #print(type(self.crt_scene))
    def next_scene(self, scene_name):
        self.crt_scene = scene_name

    def opening_scene(self):                                                    # opening description
        print("""\
        \"T1! Can you hear me? Listen, something went horribly wrong during the extraction.
        Somehow the aliens had you cornered and we had to make a break for it - the rest of the team
        and I are on our way back to Earth now. I don't know how much you remember but we last saw you at the
        central corridor. The ship is full of aliens but there is a chance that you can escape. You'll need to take a bomb
        from the armory and use it to destroy the ship. Take the bomb to the bridge and head to the pod-room.
        The resulting bomb blast can propel you towards Earth - where we'll be waiting. I know you can do this.
        One last thing - there is something strange about these aliens. To defeat them, you need to *static*...
        laugh...*static*...comedy.....\"""")


a_map = Map('central_corridor')
a_game = Engine(a_map)
player = Human(False, None, None)
a_game.play(player)
