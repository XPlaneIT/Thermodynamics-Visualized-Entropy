from manim import *
from manim_voiceover import VoiceoverScene
from _010voice_helper import EdgeTTSService

class EntropyDefinition(VoiceoverScene):
    def construct(self):
        # Initialize the voiceover service
        self.set_speech_service(EdgeTTSService(voice="en-US-AndrewNeural"))

        # ====================================================================
        # FRAME & MARGIN LAYOUT CONSTANTS
        # ====================================================================
        LEFT_COL_X = -3.4
        RIGHT_COL_X = 3.3

        # ====================================================================
        # PART 1: THE MATHEMATICAL PROOF (P-V Diagram)
        # ====================================================================
        
        # 1. Setup the P-V Diagram (Left Column)
        axes_pv = Axes(
            x_range=[0, 10, 2], y_range=[0, 10, 2],
            x_length=4.5, y_length=4.5,
            axis_config={"include_tip": True, "include_numbers": False}
        ).move_to([LEFT_COL_X, -0.2, 0])
        
        v_label = axes_pv.get_x_axis_label("V", edge=RIGHT, direction=DOWN, buff=0.15)
        p_label = axes_pv.get_y_axis_label("P", edge=UP, direction=LEFT, buff=0.15)
        
        state_1_pv = axes_pv.c2p(2, 2)
        state_2_pv = axes_pv.c2p(8, 8)
        
        dot_1 = Dot(state_1_pv, color=WHITE)
        dot_2 = Dot(state_2_pv, color=WHITE)
        label_1 = MathTex("1", font_size=24).next_to(dot_1, DOWN + LEFT, buff=0.1)
        label_2 = MathTex("2", font_size=24).next_to(dot_2, UP + RIGHT, buff=0.1)
        
        path_A = ArcBetweenPoints(state_1_pv, state_2_pv, angle=-PI/3, color=BLUE)
        path_A_label = Text("Path A", font_size=18, color=BLUE).next_to(path_A, DOWN, buff=0.2)
        
        path_B = ArcBetweenPoints(state_1_pv, state_2_pv, angle=PI/3, color=RED)
        path_B_label = Text("Path B", font_size=18, color=RED).next_to(path_B, UP, buff=0.2)

        with self.voiceover(text="Let us consider a system undergoing a reversible cycle. It goes from state 1 to state 2, and then returns to state 1.") as tracker:
            self.play(Create(axes_pv), Write(v_label), Write(p_label), run_time=tracker.duration*0.3)
            self.play(FadeIn(dot_1, label_1), FadeIn(dot_2, label_2), run_time=tracker.duration*0.2)
            self.play(Create(path_A), Write(path_A_label), run_time=tracker.duration*0.25)
            self.play(Create(path_B), Write(path_B_label), run_time=tracker.duration*0.25)
        
        # 2. The Math Derivation (Right Column)
        intro_text = Text("For a reversible cycle:", font_size=21).move_to([RIGHT_COL_X, 2.5, 0])
        
        cyclic_eq = MathTex(
            r"\oint", r"\left(\frac{\delta Q}{T}\right)_{rev}", r"=", r"0",
            font_size=30
        ).next_to(intro_text, DOWN, buff=0.35)
        
        expand_eq = MathTex(
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{A}", r"+",
            r"\int_{2}^{1}", r"\left(\frac{\delta Q}{T}\right)_{B}", r"=", r"0",
            font_size=25
        ).move_to(cyclic_eq)
        
        with self.voiceover(text="From the Clausius inequality, we know that for a reversible cycle, the cyclic integral of delta Q over T is zero. We can split this integral into the path from 1 to 2, and the path from 2 back to 1.") as tracker:
            self.play(Write(intro_text), Write(cyclic_eq), run_time=tracker.duration*0.3)
            self.wait(tracker.duration*0.1)
            self.play(TransformMatchingTex(cyclic_eq, expand_eq, path_arc=PI/4), run_time=tracker.duration*0.6)

        flip_eq = MathTex(
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{A}", r"-",
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{B}", r"=", r"0",
            font_size=25
        ).move_to(expand_eq)
        
        with self.voiceover(text="Reversing the limits on Path B introduces a negative sign.") as tracker:
            self.play(TransformMatchingTex(expand_eq, flip_eq, path_arc=PI/4), run_time=tracker.duration)

        # Term (\int_1^2 \delta Q / T)_B flies across the '=' sign to the right side!
        final_eq = MathTex(
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{A}", r"=",
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{B}",
            font_size=26
        ).move_to(flip_eq)
        
        with self.voiceover(text="Rearranging this shows that the integral along Path A is exactly equal to the integral along Path B.") as tracker:
            self.play(TransformMatchingTex(flip_eq, final_eq, path_arc=PI/2), run_time=tracker.duration)

        conclusion_text = Text(
            "The integral is path-independent!\nThis defines a property:",
            font_size=18, line_spacing=1.2, color=YELLOW
        ).next_to(final_eq, DOWN, buff=0.7)
        
        entropy_eq = MathTex(
            r"\Delta S", r"=", r"S_2 - S_1", r"=", r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{rev}",
            font_size=26, color=GREEN
        ).next_to(conclusion_text, DOWN, buff=0.45)

        entropy_box = SurroundingRectangle(entropy_eq, color=GREEN, buff=0.12)

        with self.voiceover(text="Because the integral is independent of the path taken, it depends only on the initial and final states. This means it defines a thermodynamic property. We call this property, Entropy. Delta S equals S 2 minus S 1, which equals the integral of delta Q over T along a reversible path.") as tracker:
            self.play(FadeIn(conclusion_text, shift=UP * 0.2), run_time=tracker.duration*0.2)
            self.play(TransformMatchingTex(final_eq.copy(), entropy_eq, path_arc=PI/4), run_time=tracker.duration*0.2)
           
            self.wait(tracker.duration* 0.6)
            
        
        self.wait(1)

        with self.voiceover(text="But to perform this integration, one needs to know the relation\
        between Q and T during a process. This relation is often not available, and\
        the integral can be performed for a few cases only. For the\
        majority of cases we have to rely on tabulated data for entropy") as tracker:
            
            self.play(Create(entropy_box), run_time=tracker.duration*0.2)                        
            self.wait(tracker.duration*0.8)
            

        # ====================================================================
        # PART 2: REPLACING WITH THE T-S DIAGRAM
        # ====================================================================
        part1_group = VGroup(
            axes_pv, v_label, p_label, dot_1, dot_2, label_1, label_2,
            path_A, path_A_label, path_B, path_B_label,
            intro_text, final_eq, conclusion_text, entropy_eq,
            entropy_box
        )
        self.play(FadeOut(part1_group), run_time=1.2)
        self.wait(0.4)

        # 1. Setup the T-S Diagram
        axes_ts = Axes(
            x_range=[0, 1, 0.1], y_range=[0, 5, 1],
            x_length=6.4, y_length=4.2,
            axis_config={"include_tip": True, "include_numbers": False, "stroke_width": 2},
            tips=True
        ).move_to([-0.2, -0.15, 0])
        
        t_axis_label = MathTex("T", font_size=28).next_to(axes_ts.y_axis.get_end(), UP, buff=0.1)
        s_axis_label = MathTex(r"S, \ \text{kJ/K}", font_size=26).next_to(axes_ts.x_axis.get_end(), RIGHT, buff=0.15)

        state_1_ts = axes_ts.c2p(0.3, 1.5)
        state_2_ts = axes_ts.c2p(0.7, 3.5)
        
        dot1_ts = Dot(state_1_ts, color=WHITE)
        dot2_ts = Dot(state_2_ts, color=WHITE)
        label1_ts = MathTex("1", font_size=24).next_to(dot1_ts, DOWN + LEFT, buff=0.1)
        label2_ts = MathTex("2", font_size=24).next_to(dot2_ts, UP + RIGHT, buff=0.1)

        proj_1 = DashedLine(state_1_ts, axes_ts.c2p(0.3, 0), color=GRAY)
        proj_2 = DashedLine(state_2_ts, axes_ts.c2p(0.7, 0), color=GRAY)
        
        s_val_1 = MathTex("0.3", font_size=24).next_to(axes_ts.c2p(0.3, 0), DOWN, buff=0.15)
        s_val_2 = MathTex("0.7", font_size=24).next_to(axes_ts.c2p(0.7, 0), DOWN, buff=0.15)

        # 3. The Two Paths
        path_rev = CubicBezier(
            state_1_ts,
            state_1_ts + RIGHT * 1.4 + DOWN * 0.85,
            state_2_ts + LEFT * 1.4 + DOWN * 0.85,
            state_2_ts,
            color=ORANGE, stroke_width=3.5
        )
        
        path_irrev_curve = CubicBezier(
            state_1_ts,
            state_1_ts + RIGHT * 1.4 + UP * 1.15,
            state_2_ts + LEFT * 1.4 + UP * 1.15,
            state_2_ts,
            color=ORANGE, stroke_width=3.5
        )
        path_irrev = DashedVMobject(path_irrev_curve, num_dashes=28)

        rev_p1 = path_rev.point_from_proportion(0.48)
        rev_p2 = path_rev.point_from_proportion(0.52)
        rev_dir = normalize(rev_p2 - rev_p1)
        arrow_rev = Arrow(
            start=rev_p1 - rev_dir * 0.22,
            end=rev_p1 + rev_dir * 0.22,
            color=ORANGE, buff=0, max_tip_length_to_length_ratio=0.45
        )
        
        irrev_p1 = path_irrev_curve.point_from_proportion(0.48)
        irrev_p2 = path_irrev_curve.point_from_proportion(0.52)
        irrev_dir = normalize(irrev_p2 - irrev_p1)
        arrow_irrev = Arrow(
            start=irrev_p1 - irrev_dir * 0.22,
            end=irrev_p1 + irrev_dir * 0.22,
            color=ORANGE, buff=0, max_tip_length_to_length_ratio=0.45
        )

        # 4. Labels and Pointers
        text_rev = Text("Reversible\nprocess", font_size=16, line_spacing=1.1).next_to(
            path_rev.point_from_proportion(0.62), DOWN + RIGHT, buff=0.25
        )
        pointer_rev = Line(
            text_rev.get_top() + LEFT * 0.15,
            path_rev.point_from_proportion(0.62),
            color=WHITE, stroke_width=1
        )

        text_irrev = Text("Irreversible\nprocess", font_size=16, line_spacing=1.1).next_to(
            path_irrev_curve.point_from_proportion(0.38), UP + LEFT, buff=0.25
        )
        pointer_irrev = Line(
            text_irrev.get_bottom() + RIGHT * 0.15,
            path_irrev_curve.point_from_proportion(0.38),
            color=WHITE, stroke_width=1
        )

        # 5. Top Equation & Bottom Caption
        delta_s_eq = MathTex(
            r"\Delta S = S_2 - S_1 = 0.4 \ \text{kJ/K}",
            font_size=28, color=GREEN
        ).to_edge(UP, buff=0.45)

        caption = Text(
            "The entropy change between two specified states is the same\nwhether the process is reversible or irreversible.",
            font_size=17, line_spacing=1.2
        ).to_edge(DOWN, buff=0.4)

        

        # ====================================================================
        # PART 3: ANIMATE THE T-S DIAGRAM
        # ====================================================================
        with self.voiceover(text="Let's visualize this on a Temperature-Entropy diagram. We move from state 1, at an entropy of 0.3, to state 2, at an entropy of 0.7.") as tracker:
            self.play(Create(axes_ts), Write(t_axis_label), Write(s_axis_label), run_time=tracker.duration*0.3)
            self.play(FadeIn(dot1_ts, label1_ts, dot2_ts, label2_ts), run_time=tracker.duration*0.2)
            self.play(Create(proj_1), Create(proj_2), Write(s_val_1), Write(s_val_2), run_time=tracker.duration*0.5)
        
        self.wait(0.4)
        
        with self.voiceover(text="We have an internally reversible path.") as tracker:
            self.play(Create(path_rev), FadeIn(arrow_rev), run_time=tracker.duration*0.6)
            self.play(Write(text_rev), Create(pointer_rev), run_time=tracker.duration*0.4)
        
        self.wait(0.4)
        
        with self.voiceover(text="and irreversible path.") as tracker:
            self.play(Create(path_irrev), FadeIn(arrow_irrev), run_time=tracker.duration*0.6)
            self.play(Write(text_irrev), Create(pointer_irrev), run_time=tracker.duration*0.4)
        
        self.wait(0.5)

        
        
        with self.voiceover(text="Notice, however, that the change in entropy, Delta S, is exactly the same in both cases: 0.4 kilojoules per Kelvin. The entropy change between two specified states is identical whether the process is reversible or irreversible.") as tracker:
            self.play(Write(delta_s_eq), run_time=tracker.duration*0.4)
            self.play(FadeIn(caption, shift=UP * 0.2), run_time=tracker.duration*0.4)
            self.wait(tracker.duration*0.2)


        with self.voiceover(text="The integral along an irreversible path is\
                not a property, and in general, different values will be obtained when the\
                integration is carried out along different irreversible paths. Therefore, even\
                for irreversible processes, the entropy change should be determined by carrying out this integration along some convenient imaginary internally\
                reversible path between the specified states.") as tracker:
                                    
            self.wait(tracker.duration)
            
        self.wait(2)
