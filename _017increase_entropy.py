from manim import *
from manim_voiceover import VoiceoverScene
from _010voice_helper import EdgeTTSService

class IncreaseOfEntropyPrinciple(VoiceoverScene):
    def construct(self):
        # Initialize the voiceover service
        self.set_speech_service(EdgeTTSService(voice="en-US-AndrewNeural"))

        # ====================================================================
        # FRAME & MARGIN LAYOUT CONSTANTS
        # ====================================================================
        LEFT_COL_X = -3.4
        RIGHT_COL_X = 3.3

        # ====================================================================
        # PART 1: EXTENSIVE PROPERTY & SUBSYSTEMS (Fig. 7-6)
        # ====================================================================
        title_1 = Text("The Increase of Entropy Principle", font_size=26, color=YELLOW).to_edge(UP, buff=0.4)

        # Left Column: Isolated System Box with Subsystems 1, 2, 3 ... N
        iso_outer = RoundedRectangle(
            corner_radius=0.15, width=5.2, height=4.3,
            color=GRAY, stroke_width=8, fill_color=GRAY_E, fill_opacity=0.25
        ).move_to([LEFT_COL_X, -0.35, 0])
        iso_label = Text("(Isolated)", font_size=18, color=GRAY_B).next_to(iso_outer, UP, buff=0.15)

        sub1 = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.1, color=PINK, fill_opacity=0.25).move_to(
            iso_outer.get_corner(UL) + RIGHT * 1.3 + DOWN * 0.75
        )
        sub1_txt = Text("Subsystem\n1", font_size=15, line_spacing=1.1).move_to(sub1)

        sub2 = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.1, color=LIGHT_GRAY, fill_opacity=0.25).next_to(
            sub1, DOWN, buff=0.15
        )
        sub2_txt = Text("Subsystem\n2", font_size=15, line_spacing=1.1).move_to(sub2)

        sub3 = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.1, color=PINK, fill_opacity=0.25).next_to(
            sub2, DOWN, buff=0.15
        )
        sub3_txt = Text("Subsystem\n3", font_size=15, line_spacing=1.1).move_to(sub3)

        dots_sub = MathTex(r"\cdots", font_size=30).next_to(sub3, RIGHT, buff=0.25)

        subN = RoundedRectangle(corner_radius=0.2, width=2.1, height=1.2, color=BLUE_B, fill_opacity=0.25).move_to(
            iso_outer.get_corner(DR) + LEFT * 1.25 + UP * 0.8
        )
        subN_txt = MathTex(r"\text{Subsystem } N", font_size=20).move_to(subN)

        fig76_group = VGroup(
            iso_outer, iso_label,
            sub1, sub1_txt, sub2, sub2_txt, sub3, sub3_txt, dots_sub, subN, subN_txt
        )

        # Right Column: Extensive property summation
        ext_text = Text(
            "Entropy is an extensive property:\ntotal entropy change is the sum of its parts.",
            font_size=17, line_spacing=1.2
        ).move_to([RIGHT_COL_X, 1.5, 0])

        sum_eq_1 = MathTex(
            r"\Delta S_{\text{total}}", r"=", r"\sum_{i=1}^{N} \Delta S_i", r"\geq", r"0",
            font_size=28, color=GREEN
        ).next_to(ext_text, DOWN, buff=0.45)

        sum_eq_expanded = MathTex(
            r"\Delta S_{\text{total}}", r"=", r"\Delta S_1 + \Delta S_2 + \cdots + \Delta S_N", r"\geq", r"0",
            font_size=23, color=GREEN
        ).move_to(sum_eq_1)

        # --- Animation Part 1 ---
        with self.voiceover(text="Let's discuss the increase of entropy principle. Entropy is an extensive property. This means the total entropy change of an isolated system is simply the sum of the entropy changes of its individual parts.") as tracker:
            self.play(Write(title_1), run_time=tracker.duration*0.2)
            self.play(Create(iso_outer), Write(iso_label), run_time=tracker.duration*0.2)
            self.play(
                FadeIn(sub1, sub1_txt), FadeIn(sub2, sub2_txt), FadeIn(sub3, sub3_txt),
                Write(dots_sub), FadeIn(subN, subN_txt),
                run_time=tracker.duration*0.3
            )
            self.play(Write(ext_text), Write(sum_eq_1), run_time=tracker.duration*0.3)
        
        self.wait(0.5)
        
        with self.voiceover(text="Mathematically, we can expand this as delta S one, plus delta S two, all the way to delta S N. And this total must be greater than or equal to zero.") as tracker:
            self.play(TransformMatchingTex(sum_eq_1, sum_eq_expanded, path_arc=PI/4), run_time=tracker.duration)

        self.wait(1)

        # ====================================================================
        # PART 2: SYSTEM + SURROUNDINGS = ISOLATED SYSTEM (Fig. 7-7)
        # ====================================================================
        self.play(FadeOut(fig76_group), FadeOut(ext_text))

        boundary_outer = Ellipse(
            width=5.2, height=4.6,
            color=GRAY_B, stroke_width=6, fill_color=GRAY_E, fill_opacity=0.25
        ).move_to([LEFT_COL_X, -0.35, 0])

        iso_bnd_lbl = Text("Isolated system\nboundary", font_size=14, line_spacing=1.1).move_to(
            boundary_outer.get_top() + LEFT * 1.65 + DOWN * 0.25
        )
        iso_bnd_ptr = Line(
            iso_bnd_lbl.get_right() + RIGHT * 0.05,
            boundary_outer.point_at_angle(125 * DEGREES),
            stroke_width=1.2, color=WHITE
        )

        no_transfer_lbl = MathTex(r"m = 0 \\ Q = 0 \\ W = 0", font_size=18, color=YELLOW).move_to(
            boundary_outer.get_top() + RIGHT * 1.55 + DOWN * 0.35
        )
        no_transfer_arr = CurvedArrow(
            no_transfer_lbl.get_left() + LEFT * 0.05,
            boundary_outer.get_top() + DOWN * 0.75 + RIGHT * 0.35,
            angle=0.35, tip_length=0.14, stroke_width=1.5, color=YELLOW
        )

        cyl_left_top = Line([LEFT_COL_X - 0.95, 0.75, 0], [LEFT_COL_X - 0.95, -0.95, 0], color=WHITE, stroke_width=3)
        cyl_inlet_top = Line([LEFT_COL_X - 0.95, -0.95, 0], [LEFT_COL_X - 1.25, -0.95, 0], color=WHITE, stroke_width=3)
        cyl_inlet_bot = Line([LEFT_COL_X - 1.25, -1.15, 0], [LEFT_COL_X - 0.95, -1.15, 0], color=WHITE, stroke_width=3)
        cyl_bottom_right = VMobject(color=WHITE, stroke_width=3).set_points_as_corners([
            [LEFT_COL_X - 0.95, -1.15, 0], [LEFT_COL_X - 0.95, -1.35, 0],
            [LEFT_COL_X + 0.95, -1.35, 0], [LEFT_COL_X + 0.95, 0.75, 0]
        ])

        piston = Rectangle(width=1.86, height=0.25, color=GRAY_A, fill_color=GRAY, fill_opacity=0.9, stroke_width=1.5).move_to([LEFT_COL_X, 0.25, 0])

        sys_box = DashedVMobject(
            Rectangle(width=1.72, height=1.35, color=ORANGE, stroke_width=2.5).move_to([LEFT_COL_X, -0.6, 0]),
            num_dashes=26
        )
        sys_lbl = Text("System", font_size=16).move_to(sys_box.get_center() + UP * 0.25)
        surr_lbl = Text("Surroundings", font_size=16, color=GRAY_A).move_to([LEFT_COL_X, -1.85, 0])

        m_arrow_in = CurvedArrow([LEFT_COL_X - 1.65, -0.85, 0], [LEFT_COL_X - 1.05, -1.02, 0], angle=0.3, tip_length=0.12, stroke_width=1.5)
        m_arrow_out = CurvedArrow([LEFT_COL_X - 1.05, -1.10, 0], [LEFT_COL_X - 1.65, -1.00, 0], angle=-0.3, tip_length=0.12, stroke_width=1.5)
        m_lbl = MathTex("m", font_size=20).next_to(m_arrow_in, UP, buff=0.05)

        qw_arrow_out = CurvedArrow([LEFT_COL_X + 0.65, -0.85, 0], [LEFT_COL_X + 1.45, -0.95, 0], angle=-0.2, tip_length=0.12, stroke_width=1.5)
        qw_arrow_in = CurvedArrow([LEFT_COL_X + 1.45, -1.12, 0], [LEFT_COL_X + 0.65, -1.02, 0], angle=0.2, tip_length=0.12, stroke_width=1.5)
        qw_lbl = MathTex("Q, W", font_size=20).next_to(qw_arrow_out, UP, buff=0.05)

        # Right Column: Eq (7-11) Derivation
        sys_surr_txt = Text(
            "System + Surroundings = Isolated System\n(No entropy transfer across outer boundary):",
            font_size=16, line_spacing=1.2
        ).move_to([RIGHT_COL_X, 2.25, 0])

        eq_711_step1 = MathTex(
            r"\Delta S_{\text{total}}", r"=", r"\Delta S_{\text{sys}}", r"+", r"\Delta S_{\text{surr}}", r"\geq", r"0",
            font_size=24
        ).move_to(sum_eq_expanded)

        eq_711_final = MathTex(
            r"S_{\text{gen}}", r"=", r"\Delta S_{\text{total}}", r"=", r"\Delta S_{\text{sys}}", r"+", r"\Delta S_{\text{surr}}", r"\geq", r"0",
            font_size=22, color=GREEN
        ).move_to(eq_711_step1)

        eq_711_box = SurroundingRectangle(eq_711_final, color=GREEN, buff=0.1)

        # --- Animation Part 2 ---
        with self.voiceover(text="We can define an isolated system as the combination of a system and its surroundings. Because it is isolated, no mass, heat, or work can cross the outer boundary.") as tracker:
            self.play(Create(boundary_outer), Write(iso_bnd_lbl), Create(iso_bnd_ptr), run_time=tracker.duration*0.25)
            self.play(Write(no_transfer_lbl), Create(no_transfer_arr), run_time=tracker.duration*0.25)
            self.play(
                Create(cyl_left_top), Create(cyl_inlet_top), Create(cyl_inlet_bot), Create(cyl_bottom_right),
                FadeIn(piston), Create(sys_box), Write(sys_lbl), Write(surr_lbl),
                run_time=tracker.duration*0.25
            )
            self.play(
                Create(m_arrow_in), Create(m_arrow_out), Write(m_lbl),
                Create(qw_arrow_out), Create(qw_arrow_in), Write(qw_lbl),
                run_time=tracker.duration*0.25
            )

        with self.voiceover(text="Therefore, the total entropy change is the sum of the entropy change of the system, plus the entropy change of the surroundings.") as tracker:
            self.play(Write(sys_surr_txt), run_time=tracker.duration*0.3)
            self.play(TransformMatchingTex(sum_eq_expanded, eq_711_step1, path_arc=PI/3), run_time=tracker.duration*0.7)

        with self.voiceover(text="This total is equal to the entropy generation. And by the increase of entropy principle, entropy generation must be greater than or equal to zero.") as tracker:
            self.play(TransformMatchingTex(eq_711_step1, eq_711_final, path_arc=PI/4), run_time=tracker.duration*0.7)
            self.play(Create(eq_711_box), run_time=tracker.duration*0.3)

        self.wait(1)

        # ====================================================================
        # PART 3: NEGATIVE SYSTEM ENTROPY CHANGE EXAMPLE (Fig. 7-8)
        # ====================================================================
        fig77_only = VGroup(
            iso_bnd_lbl, iso_bnd_ptr, no_transfer_lbl, no_transfer_arr,
            m_arrow_in, m_arrow_out, m_lbl, qw_arrow_out, qw_arrow_in, qw_lbl,
            sys_lbl, surr_lbl
        )
        self.play(FadeOut(fig77_only), FadeOut(sys_surr_txt))

        surr_top_78 = Text("Surroundings", font_size=16, color=GRAY_A).move_to([LEFT_COL_X, 1.45, 0])
        ds_sys_78 = MathTex(r"\Delta S_{\text{sys}} = -2\text{ kJ/K}", font_size=20, color=RED).move_to([LEFT_COL_X, -0.35, 0])
        sys_caps_78 = Text("SYSTEM", font_size=15).move_to([LEFT_COL_X, -0.8, 0])
        ds_surr_78 = MathTex(r"\Delta S_{\text{surr}} = 3\text{ kJ/K}", font_size=20, color=ORANGE).move_to([LEFT_COL_X, -1.8, 0])

        q_out_arrow = Arrow(
            [LEFT_COL_X + 0.55, -0.95, 0], [LEFT_COL_X + 1.55, -0.95, 0],
            color=ORANGE, stroke_width=5, max_tip_length_to_length_ratio=0.35
        )
        q_out_lbl = MathTex("Q", font_size=22, color=ORANGE).next_to(q_out_arrow, RIGHT, buff=0.1)

        neg_note = Text(
            "A system's entropy can decrease (heat rejection),\nbut entropy generation CANNOT be negative:",
            font_size=16, line_spacing=1.2, color=YELLOW
        ).move_to([RIGHT_COL_X, 2.25, 0])

        num_eq = MathTex(
            r"S_{\text{gen}}", r"=", r"-2", r"+", r"3", r"=", r"+1\text{ kJ/K} > 0",
            font_size=24, color=WHITE
        ).next_to(eq_711_box, DOWN, buff=0.35)

        criteria_box_title = Text("Increase of Entropy Principle:", font_size=17, color=YELLOW).next_to(num_eq, DOWN, buff=0.45)
        crit_irrev = MathTex(r"S_{\text{gen}} > 0 \quad \Rightarrow \quad \text{Irreversible process}", font_size=21, color=GREEN)
        crit_rev = MathTex(r"S_{\text{gen}} = 0 \quad \Rightarrow \quad \text{Reversible process}", font_size=21, color=BLUE_B)
        crit_imp = MathTex(r"S_{\text{gen}} < 0 \quad \Rightarrow \quad \text{Impossible process}", font_size=21, color=RED)

        criteria_group = VGroup(crit_irrev, crit_rev, crit_imp).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(
            criteria_box_title, DOWN, buff=0.25
        )

        # --- Animation Part 3 ---
        with self.voiceover(text="Let's look at a numerical example. A system rejects heat, so its entropy decreases by 2 kilojoules per Kelvin.") as tracker:
            self.play(
                Write(surr_top_78), Write(ds_sys_78), Write(sys_caps_78),
                GrowArrow(q_out_arrow), Write(q_out_lbl),
                run_time=tracker.duration*0.6
            )
            self.play(Write(neg_note), run_time=tracker.duration*0.4)

        with self.voiceover(text="However, the surroundings absorb this heat, and their entropy increases by 3. The entropy generation is positive 1, proving this process is possible and irreversible.") as tracker:
            self.play(Write(ds_surr_78), run_time=tracker.duration*0.3)
            self.play(TransformMatchingTex(eq_711_final.copy(), num_eq, path_arc=PI/4), run_time=tracker.duration*0.7)

        with self.voiceover(text="This gives us our three criteria. A positive entropy generation means an irreversible process. Zero means a reversible process. And a negative value is impossible.") as tracker:
            self.play(Write(criteria_box_title), run_time=tracker.duration*0.2)
            self.play(FadeIn(criteria_group, shift=UP * 0.15, lag_ratio=0.25), run_time=tracker.duration*0.8)

        self.wait(1.5)

        # ====================================================================
        # PART 4: KEY REMARKS ABOUT ENTROPY (Centered Summary)
        # ====================================================================
        everything_part3 = VGroup(
            boundary_outer, cyl_left_top, cyl_inlet_top, cyl_inlet_bot, cyl_bottom_right,
            piston, sys_box, surr_top_78, ds_sys_78, sys_caps_78, ds_surr_78,
            q_out_arrow, q_out_lbl,
            neg_note, eq_711_final, eq_711_box, num_eq, criteria_box_title, criteria_group
        )
        
        remarks_header = Text("Key Conclusions About Entropy", font_size=24, color=GREEN).next_to(title_1, DOWN, buff=0.45)

        r1 = VGroup(
            Text("1. Direction of Processes:", font_size=19, color=YELLOW),
            Text("Processes occur in one direction only (S_gen ≥ 0). Violations are impossible,\noften halting chemical reactions before full completion.", font_size=16, line_spacing=1.15)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        r2 = VGroup(
            Text("2. Nonconserved Property:", font_size=19, color=YELLOW),
            Text("There is no conservation of entropy principle. Entropy is conserved only in\nidealized reversible processes and increases during all actual processes.", font_size=16, line_spacing=1.15)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        r3 = VGroup(
            Text("3. Measure of Irreversibility & Equilibrium:", font_size=19, color=YELLOW),
            Text("Entropy generation quantifies irreversibilities that degrade engineering\ndevices. Isolated systems evolve until entropy reaches a maximum (equilibrium).", font_size=16, line_spacing=1.15)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        remarks_list = VGroup(r1, r2, r3).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(remarks_header, DOWN, buff=0.4)

        # --- Animation Part 4 ---
        with self.voiceover(text="To summarize the key conclusions: First, processes have a strict direction. Violations are impossible, which often halts chemical reactions before they reach full completion.") as tracker:
            self.play(FadeOut(everything_part3), run_time=tracker.duration*0.3)
            self.play(Write(remarks_header), run_time=tracker.duration*0.2)
            self.play(FadeIn(r1, shift=RIGHT * 0.2), run_time=tracker.duration*0.5)
        
        self.wait(0.5)
        
        with self.voiceover(text="Second, entropy is not a conserved property. It is conserved only in idealized reversible processes, and always increases during actual processes.") as tracker:
            self.play(FadeIn(r2, shift=RIGHT * 0.2), run_time=tracker.duration)
            
        self.wait(0.5)
        
        with self.voiceover(text="Finally, entropy generation is a measure of irreversibility that degrades engineering devices. Isolated systems will evolve until entropy reaches a maximum, which is the state of equilibrium.\
            We will conclude here for now. Perhaps you were expecting me to say that entropy is a measure of disorder—like how your room will get messy over time—but that is just one aspect of the probabilistic view of entropy.") as tracker:
            self.play(FadeIn(r3, shift=RIGHT * 0.2), run_time=tracker.duration * 0.1)
            self.wait(tracker.duration* 0.9)
            
        self.wait(3)

