from manim import *
from manim_voiceover import VoiceoverScene
from _010voice_helper import EdgeTTSService

class EntropyGeneration(VoiceoverScene):
    def construct(self):
        # Initialize the voiceover service
        self.set_speech_service(EdgeTTSService(voice="en-US-AndrewNeural"))

        # ====================================================================
        # FRAME & MARGIN LAYOUT CONSTANTS
        # ====================================================================
        LEFT_COL_X = -3.4
        RIGHT_COL_X = 3.3

        # ====================================================================
        # 1. SETUP THE T-S DIAGRAM
        # ====================================================================
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 5, 1],
            x_length=4.5, y_length=4.5,
            axis_config={"include_tip": True, "include_numbers": False}
        ).move_to([LEFT_COL_X, -0.3, 0])
        
        t_label = axes.get_y_axis_label("T", edge=UP, direction=LEFT, buff=0.15)
        s_label = axes.get_x_axis_label("S", edge=RIGHT, direction=DOWN, buff=0.15)

        state_1 = axes.c2p(1.0, 1.3)
        state_2 = axes.c2p(4.0, 4.2)
        
        dot1 = Dot(state_1, color=WHITE)
        dot2 = Dot(state_2, color=WHITE)
        label1 = MathTex("1", font_size=24).next_to(dot1, DOWN + LEFT, buff=0.1)
        label2 = MathTex("2", font_size=24).next_to(dot2, UP + RIGHT, buff=0.1)

        path_12_curve = CubicBezier(
            state_1,
            state_1 + RIGHT * 1.2 + UP * 2.0,
            state_2 + LEFT * 1.6 + UP * 0.4,
            state_2,
            color=ORANGE, stroke_width=3.5
        )
        path_12 = DashedVMobject(path_12_curve, num_dashes=26)
        
        path_21 = CubicBezier(
            state_2,
            state_2 + LEFT * 1.2 + DOWN * 2.0,
            state_1 + RIGHT * 1.6 + DOWN * 0.4,
            state_1,
            color=ORANGE, stroke_width=3.5
        )

        p12_a = path_12_curve.point_from_proportion(0.48)
        p12_b = path_12_curve.point_from_proportion(0.52)
        dir_12 = normalize(p12_b - p12_a)
        arrow_12 = Arrow(
            start=p12_a - dir_12 * 0.22,
            end=p12_a + dir_12 * 0.22,
            color=ORANGE, buff=0, max_tip_length_to_length_ratio=0.45
        )

        p21_a = path_21.point_from_proportion(0.48)
        p21_b = path_21.point_from_proportion(0.52)
        dir_21 = normalize(p21_b - p21_a)
        arrow_21 = Arrow(
            start=p21_a - dir_21 * 0.22,
            end=p21_a + dir_21 * 0.22,
            color=ORANGE, buff=0, max_tip_length_to_length_ratio=0.45
        )

        text_12 = Text(
            "Process 1-2\n(reversible or\nirreversible)",
            font_size=15, line_spacing=1.1
        ).next_to(path_12_curve.point_from_proportion(0.35), UP + LEFT, buff=0.25)
        ptr_12 = Line(
            text_12.get_bottom() + RIGHT * 0.2,
            path_12_curve.point_from_proportion(0.35),
            color=WHITE, stroke_width=1
        )

        text_21 = Text(
            "Process 2-1\n(internally\nreversible)",
            font_size=15, line_spacing=1.1
        ).next_to(path_21.point_from_proportion(0.35), DOWN + RIGHT, buff=0.25)
        ptr_21 = Line(
            text_21.get_top() + LEFT * 0.2,
            path_21.point_from_proportion(0.35),
            color=WHITE, stroke_width=1
        )

        # ====================================================================
        # 2. THE MATHEMATICAL DERIVATION
        # ====================================================================
        eq1 = MathTex(
            r"\oint", r"\frac{\delta Q}{T}", r"\leq", r"0",
            font_size=34
        ).move_to([RIGHT_COL_X, 2.7, 0])

        eq2 = MathTex(
            r"\int_{1}^{2}", r"\frac{\delta Q}{T}", r"+", r"\int_{2}^{1} \left(\frac{\delta Q}{T}\right)_{rev}", r"\leq", r"0",
            font_size=28
        ).move_to([RIGHT_COL_X, 1.4, 0])

        highlight_rev = SurroundingRectangle(eq2[3], color=YELLOW, buff=0.08)

        eq3 = MathTex(
            r"\int_{1}^{2}", r"\frac{\delta Q}{T}", r"+", r"(", r"S_1", r"-", r"S_2", r")", r"\leq", r"0",
            font_size=29
        ).move_to(eq2)

        eq4 = MathTex(
            r"S_2", r"-", r"S_1", r"\geq", r"\int_{1}^{2}", r"\frac{\delta Q}{T}",
            font_size=32
        ).move_to([RIGHT_COL_X, 1.3, 0])

        eq5 = MathTex(
            r"dS", r"\geq", r"\frac{\delta Q}{T}",
            font_size=32, color=YELLOW
        ).move_to([RIGHT_COL_X, 0.0, 0])
        
        eq6 = MathTex(
            r"\Delta S", r"=", r"\int_{1}^{2}", r"\frac{\delta Q}{T}", r"+", r"S_{gen}",
            font_size=32
        ).move_to(eq4)

        eq6_box = SurroundingRectangle(eq6, color=GREEN, buff=0.12)
        sgen_cond = MathTex(r"S_{gen} \geq 0", font_size=28, color=RED).next_to(eq6_box, DOWN, buff=0.25)

        # ====================================================================
        # 3. ANIMATION BLOCKS WITH VOICEOVER
        # ====================================================================

        # Block 1: The Diagram
        with self.voiceover(text="Consider a cycle made of two processes. Process 1 to 2 is arbitrary. It could be reversible or irreversible. Process 2 to 1 is internally reversible.") as tracker:
            self.play(Create(axes), Write(t_label), Write(s_label), run_time=tracker.duration*0.2)
            self.play(FadeIn(dot1, label1, dot2, label2), run_time=tracker.duration*0.2)
            self.play(Create(path_12), FadeIn(arrow_12), Write(text_12), Create(ptr_12), run_time=tracker.duration*0.3)
            self.play(Create(path_21), FadeIn(arrow_21), Write(text_21), Create(ptr_21), run_time=tracker.duration*0.3)
        self.wait(0.5)

        # Block 2: Clausius Inequality
        with self.voiceover(text="From the Clausius inequality, the cyclic integral of delta Q over T must be less than or equal to zero.") as tracker:
            self.play(Write(eq1), run_time=tracker.duration)
        self.wait(0.5)

        # Block 3: Splitting the Integral
        with self.voiceover(text="We can split this integral into the path from 1 to 2, plus the reversible path from 2 back to 1.") as tracker:
            self.play(TransformMatchingTex(eq1.copy(), eq2, path_arc=PI/4), run_time=tracker.duration)
        self.wait(0.5)

        # Block 4: Replacing with Entropy
        with self.voiceover(text="Since process 2 to 1 is internally reversible, we can replace that specific integral with the change in entropy, S 1 minus S 2.") as tracker:
            self.play(Create(highlight_rev), run_time=tracker.duration*0.3)
            self.play(FadeOut(highlight_rev), TransformMatchingTex(eq2, eq3, path_arc=PI/4), run_time=tracker.duration*0.7)
        self.wait(0.5)

        # Block 5: Rearranging
        with self.voiceover(text="Rearranging this inequality, the entropy change from state 1 to 2 is greater than or equal to the integral of delta Q over T.") as tracker:
            self.play(TransformMatchingTex(eq3, eq4, path_arc=PI/2, key_map={r"\leq": r"\geq"}), run_time=tracker.duration)
        self.wait(0.5)

        # Block 6: Differential Form
        with self.voiceover(text="In differential form, this gives us d S is greater than or equal to delta Q over T.") as tracker:
            self.play(TransformMatchingTex(eq4.copy(), eq5, path_arc=PI/4), run_time=tracker.duration)
        self.wait(0.5)

        # Block 7: Entropy Generation
        with self.voiceover(text="To make this an equality, we introduce entropy generation, S gen. This represents the entropy created by irreversibilities. By definition, S gen is always greater than or equal to zero.") as tracker:
            self.play(TransformMatchingTex(eq4, eq6, path_arc=PI/3, key_map={r"\geq": r"="}), run_time=tracker.duration*0.4)
            self.play(eq5.animate.move_to([RIGHT_COL_X, -1.5, 0]), Create(eq6_box), Write(sgen_cond), run_time=tracker.duration*0.6)
        self.wait(1)

        # Block 8: Increase of Entropy Principle
        isolated_text = Text(
            "For an isolated system\n(or adiabatic closed system), Q = 0:",
            font_size=20, line_spacing=1.2, color=WHITE
        ).move_to([RIGHT_COL_X, 1.5, 0])

        isolated_eq = MathTex(
            r"\Delta S_{isolated} \geq 0",
            font_size=42, color=YELLOW
        ).next_to(isolated_text, DOWN, buff=0.45)

        isolated_box = SurroundingRectangle(isolated_eq, color=YELLOW, buff=0.15)

        principle_text = Text(
            "The entropy of an isolated system\nalways increases or remains constant.\nIt never decreases.",
            font_size=19, line_spacing=1.2, color=GREEN
        ).next_to(isolated_box, DOWN, buff=0.55)

        with self.voiceover(text="For an isolated system, there is no heat transfer, so Q equals zero. This leads us to the increase of entropy principle. The entropy of an isolated system always increases, or in the limiting case of a reversible process, remains constant. It never decreases.") as tracker:
            self.play(FadeOut(eq1, eq5, eq6, sgen_cond, eq6_box), run_time=tracker.duration*0.2)
            self.play(Write(isolated_text), run_time=tracker.duration*0.2)
            self.play(Write(isolated_eq), Create(isolated_box), run_time=tracker.duration*0.3)
            self.play(FadeIn(principle_text, shift=UP * 0.2), run_time=tracker.duration*0.3)
            
        self.wait(2)

        