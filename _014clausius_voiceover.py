from manim import *
from manim_voiceover import VoiceoverScene
from _010voice_helper import EdgeTTSService

class ClausiusInequalityDiagram(VoiceoverScene):
    def construct(self):
        # Initialize the voiceover service
        self.set_speech_service(EdgeTTSService(voice="en-US-AndrewNeural"))

        # ====================================================================
        # 1. SETTING UP COLORS AND STYLES
        # ====================================================================
        PINK_FILL = "#F9C6D9"
        PINK_STROKE = "#E872A0"
        
        # ====================================================================
        # 2. BUILDING THE DIAGRAM (Static Elements)
        # ====================================================================
        reservoir_shape = RoundedRectangle(
            corner_radius=0.3, width=4, height=0.5,
            fill_color=RED, fill_opacity=0.8, stroke_color=PINK_STROKE, stroke_width=1
        ).to_edge(UP, buff=0.5)
        
        reservoir_text = VGroup(
            Text("Thermal reservoir at ", font_size=20),
            MathTex("T_R", font_size=24)
        ).arrange(RIGHT, buff=0.1).move_to(reservoir_shape.get_center())
        
        reservoir = VGroup(reservoir_shape, reservoir_text)

        device_circle = Circle(
            radius=0.6, fill_color=PINK_FILL, fill_opacity=0.3, 
            stroke_color=PINK_STROKE, stroke_width=2
        ).shift(UP * 1)
        
        icon = VGroup(
            Circle(radius=0.1, color=WHITE, stroke_width=3),
            Rectangle(width=0.4, height=0.1, color=WHITE, fill_opacity=1).shift(UP*0.4),
            Rectangle(width=0.3, height=0.15, color=WHITE, fill_opacity=1).shift(RIGHT*0.6),
        ).move_to(device_circle.get_center())
        
        device_text = Text(
            "Reversible\ncyclic\ndevice", font_size=16, line_spacing=0.8
        ).next_to(device_circle, LEFT, buff=0.1)
        
        device = VGroup(device_circle, icon, device_text)

        system_rect = Rectangle(
            width=1.4, height=0.8, color=WHITE, stroke_width=2
        ).shift(DOWN * 1.4)
        
        system_text = Text("System", font_size=20).move_to(system_rect.get_center())
        temp_label = MathTex("T", font_size=24).next_to(system_rect, UP, buff=0.1).shift(LEFT*0.8)
        
        system = VGroup(system_rect, system_text, temp_label)

        rect_shape = Rectangle(width=3, height=4.2, color=WHITE, stroke_width=2)
        dashed_box = DashedVMobject(rect_shape, num_dashes=50).shift(LEFT * 0.5)
        
        box_label = Text(
            "Combined system\n(system and cyclic device)", font_size=16, line_spacing=0.8
        ).next_to(dashed_box, DOWN * 0.5, buff=0.2)

        dq_r_arrow = Arrow(
            reservoir_shape.get_bottom(), device_circle.get_top(), 
            buff=0, stroke_width=4, color=WHITE, max_tip_length_to_length_ratio=0.2
        )
        dq_r_label = MathTex(r"\delta Q_R", font_size=24).next_to(dq_r_arrow, RIGHT, buff=0.1)

        dq_arrow = Arrow(
            device_circle.get_bottom(), system_rect.get_top(), 
            buff=0, stroke_width=4, color=WHITE, max_tip_length_to_length_ratio=0.2
        )
        dq_label = MathTex(r"\delta Q", font_size=24).next_to(dq_arrow, RIGHT, buff=0.1)

        dw_rev_arrow = Arrow(
            device_circle.get_right(), device_circle.get_right() + RIGHT*2, 
            buff=0, stroke_width=4, color=WHITE, max_tip_length_to_length_ratio=0.2
        )
        dw_rev_label = MathTex(r"\delta W_{rev}", font_size=24).next_to(dw_rev_arrow, UP, buff=0.05)

        dw_sys_arrow = Arrow(
            system_rect.get_right(), system_rect.get_right() + RIGHT*2, 
            buff=0, stroke_width=4, color=WHITE, max_tip_length_to_length_ratio=0.2
        )
        dw_sys_label = MathTex(r"\delta W_{sys}", font_size=24).next_to(dw_sys_arrow, UP, buff=0.05)

        diagram = VGroup(
            dashed_box, box_label,
            system, device, reservoir,
            dq_r_arrow, dq_r_label,
            dq_arrow, dq_label,
            dw_rev_arrow, dw_rev_label,
            dw_sys_arrow, dw_sys_label
        )

        # ====================================================================
        # 3. ANIMATION WITH VOICEOVER
        # ====================================================================
        
        with self.voiceover(text="To demonstrate the validity of the Clausius inequality, consider a system connected to a thermal reservoir at a constant temperature T R, through a reversible cyclic device.") as tracker:
            self.play(FadeIn(diagram), run_time=tracker.duration)
        self.wait(0.5)

        # Pointer animation
        pointer = Arrow(ORIGIN, RIGHT, color=YELLOW, stroke_width=6, max_tip_length_to_length_ratio=0.3)
        
        with self.voiceover(text="Let us identify the components. First, the thermal reservoir.") as tracker:
            pointer.next_to(reservoir, LEFT, buff=0.2)
            self.play(FadeIn(pointer), run_time=tracker.duration)
            
        with self.voiceover(text="Next, the reversible cyclic device.") as tracker:
            self.play(pointer.animate.next_to(device_text, LEFT, buff=0.2), run_time=tracker.duration)
            
        with self.voiceover(text="The device receives heat delta Q R from the reservoir.") as tracker:
            self.play(pointer.animate.next_to(dq_r_label, RIGHT, buff=0.2).rotate(PI), run_time=tracker.duration)
            
        with self.voiceover(text="It supplies heat delta Q to the system, at a boundary temperature T.") as tracker:
            self.play(pointer.animate.next_to(temp_label, LEFT, buff=0.2).rotate(PI), run_time=tracker.duration)
            
        with self.voiceover(text="The reversible device produces work, delta W rev.") as tracker:
            self.play(pointer.animate.next_to(dw_rev_label, UP, buff=0.2).rotate(-PI/2), run_time=tracker.duration)
            
        with self.voiceover(text="And the system itself produces work, delta W sys.") as tracker:
            self.play(pointer.animate.next_to(dw_sys_label, UP, buff=0.2), run_time=tracker.duration)
            self.play(FadeOut(pointer))

        # Zoom and Push left
        with self.voiceover(text="The dashed lines identify the combined system, which includes both the system and the cyclic device.") as tracker:
            self.play(dashed_box.animate.scale(1.1), run_time=0.3, rate_func=there_and_back)
            self.play(dashed_box.animate.scale(1.1), run_time=0.3, rate_func=there_and_back)
            # Wait for the rest of the audio while pushing left
            remaining_time = max(0.1, tracker.duration - 0.6)
            self.play(diagram.animate.to_edge(LEFT, buff=0.5), run_time=remaining_time)

        # --- BLOCK 1: Energy Balance ---
        dQ_R = dq_r_label.copy()
        dW_rev = dw_rev_label.copy()
        dW_sys = dw_sys_label.copy()

        eq1_lhs = MathTex(r"\delta W_C", font_size=24)
        equals = MathTex("=", font_size=24)
        plus = MathTex("+", font_size=24)
        target_rev = dW_rev.copy()
        target_sys = dW_sys.copy()

        row1_targets = VGroup(eq1_lhs, equals, target_rev, plus, target_sys).arrange(RIGHT, buff=0.15)
        row1_targets.move_to(RIGHT * 2.5 + UP * 2.5)
        
        with self.voiceover(text="Applying an energy balance to the combined system, the total work d W C is the sum of the work from the reversible device and the system.") as tracker:
            self.play(
                dW_rev.animate.move_to(target_rev),
                dW_sys.animate.move_to(target_sys),
                run_time=tracker.duration * 0.6
            )
            self.play(FadeIn(eq1_lhs, equals, plus), run_time=tracker.duration * 0.4)
        self.wait(0.5)
        
        self.play(FadeOut(dW_rev, plus, dW_sys))
        
        eq2_rhs = MathTex(r"- \delta E_C", font_size=24)
        target_dqr = dQ_R.copy()
        row2_rhs = VGroup(target_dqr, eq2_rhs).arrange(RIGHT, buff=0.15)
        row2_rhs.next_to(equals, RIGHT, buff=0.15)

        with self.voiceover(text="This total work must equal the net heat entering the combined system, delta Q R, minus the change in total energy, d E C.") as tracker:
            self.play(dQ_R.animate.move_to(target_dqr), run_time=tracker.duration * 0.6)
            self.play(FadeIn(eq2_rhs), run_time=tracker.duration * 0.4)
        self.wait(0.5)

        # --- BLOCK 2 & 3: Reversible Device Relation ---
        dQ_R_2 = dq_r_label.copy()
        dQ = dq_label.copy()
        T = system[2].copy()
        T_R = reservoir[1][1].copy()

        target_dqr_2 = dQ_R_2.copy()
        target_tr = T_R.copy()
        target_dq = dQ.copy()
        target_t = T.copy()

        bar_left = Line(LEFT * 0.35, RIGHT * 0.35, stroke_width=1.5)
        frac_left = VGroup(target_dqr_2, bar_left, target_tr).arrange(DOWN, buff=0.1)

        equals_2 = MathTex("=", font_size=24)

        bar_right = Line(LEFT * 0.25, RIGHT * 0.25, stroke_width=1.5)
        frac_right = VGroup(target_dq, bar_right, target_t).arrange(DOWN, buff=0.1)

        row3_targets = VGroup(frac_left, equals_2, frac_right).arrange(RIGHT, buff=0.2)
        row3_targets.next_to(row1_targets, DOWN, buff=0.8)

        with self.voiceover(text="Since the cyclic device is internally reversible, the heat transfer ratio equals the absolute temperature ratio.") as tracker:
            self.play(
                dQ_R_2.animate.move_to(target_dqr_2),
                T_R.animate.move_to(target_tr),
                dQ.animate.move_to(target_dq),
                T.animate.move_to(target_t),
                run_time=tracker.duration * 0.7
            )
            self.play(Create(bar_left), Create(bar_right), FadeIn(equals_2), run_time=tracker.duration * 0.3)
        self.wait(0.5)

        solved_dqr = dQ_R_2.copy()
        solved_eq = equals_2.copy()
        solved_tr = T_R.copy()
        left_paren = MathTex(r"\left(", font_size=28)
        solved_dq = dQ.copy()
        solved_bar = bar_right.copy()
        solved_t = T.copy()
        right_paren = MathTex(r"\right)", font_size=28)

        solved_frac = VGroup(solved_dq, solved_bar, solved_t).arrange(DOWN, buff=0.1)
        solved_row = VGroup(
            solved_dqr, solved_eq, solved_tr, left_paren, solved_frac, right_paren
        ).arrange(RIGHT, buff=0.12)
        solved_row.move_to(row3_targets.get_center())

        with self.voiceover(text="Rearranging this equation to solve for delta Q R yields T R multiplied by delta Q over T.") as tracker:
            self.play(
                FadeOut(bar_left),
                dQ_R_2.animate.move_to(solved_dqr),
                equals_2.animate.move_to(solved_eq),
                T_R.animate.move_to(solved_tr),
                dQ.animate.move_to(solved_dq),
                bar_right.animate.move_to(solved_bar),
                T.animate.move_to(solved_t),
                FadeIn(left_paren, right_paren),
                run_time=tracker.duration
            )
        self.wait(0.5)

        # --- BLOCK 4: Substitution ---
        rhs_expr = VGroup(T_R, left_paren, dQ, bar_right, T, right_paren)
        rhs_copy = rhs_expr.copy()

        sub_rhs_target = rhs_copy.copy()
        sub_dec_target = eq2_rhs.copy()

        top_sub_targets = VGroup(sub_rhs_target, sub_dec_target).arrange(RIGHT, buff=0.15)
        top_sub_targets.next_to(equals, RIGHT, buff=0.15)

        sub_arrow = CurvedArrow(
            rhs_expr.get_top() + UP * 0.1,
            dQ_R.get_bottom() + DOWN * 0.1,
            angle=-0.4,
            color=YELLOW,
            stroke_width=2
        )
        
        with self.voiceover(text="Substituting this expression for delta Q R back into our energy balance equation...") as tracker:
            self.play(Create(sub_arrow), run_time=tracker.duration * 0.4)
            self.play(
                FadeOut(dQ_R, sub_arrow),
                eq2_rhs.animate.move_to(sub_dec_target),
                rhs_copy.animate.move_to(sub_rhs_target),
                run_time=tracker.duration * 0.6
            )
        self.wait(0.5)

        # Fade out helper equation
        self.play(FadeOut(dQ_R_2, equals_2, rhs_expr))
        self.wait(0.5)

        # --- BLOCK 5: Cyclic Integral ---
        tr_top = rhs_copy[0]
        frac_group = VGroup(rhs_copy[1], rhs_copy[2], rhs_copy[3], rhs_copy[4], rhs_copy[5])

        oint_1 = MathTex(r"\oint", font_size=28)
        oint_2 = MathTex(r"\oint", font_size=28)
        oint_3 = MathTex(r"\oint", font_size=28)
        minus_sign = MathTex("-", font_size=24)
        dec_term = MathTex(r"\delta E_C", font_size=24)

        t_oint1 = oint_1.copy()
        t_dwc = eq1_lhs.copy()
        t_eq = equals.copy()
        t_tr = tr_top.copy()
        t_oint2 = oint_2.copy()
        t_frac = frac_group.copy()
        t_minus = minus_sign.copy()
        t_oint3 = oint_3.copy()
        t_dec = dec_term.copy()

        cyc_row = VGroup(
            t_oint1, t_dwc, t_eq, t_tr, t_oint2, t_frac, t_minus, t_oint3, t_dec
        ).arrange(RIGHT, buff=0.12)
        cyc_row.move_to(RIGHT * 2.2 + UP * 1.5)

        with self.voiceover(text="Now, we integrate this equation over a complete cycle. The cyclic integral of d E C is zero, because energy is a property, and its net change over a cycle is zero.") as tracker:
            self.play(
                FadeOut(eq2_rhs),
                FadeIn(oint_1, oint_2, minus_sign, oint_3, dec_term),
                oint_1.animate.move_to(t_oint1),
                eq1_lhs.animate.move_to(t_dwc),
                equals.animate.move_to(t_eq),
                tr_top.animate.move_to(t_tr),
                oint_2.animate.move_to(t_oint2),
                frac_group.animate.move_to(t_frac),
                minus_sign.animate.move_to(t_minus),
                oint_3.animate.move_to(t_oint3),
                dec_term.animate.move_to(t_dec),
                run_time=tracker.duration * 0.6
            )
            
            energy_term = VGroup(minus_sign, oint_3, dec_term)
            slash = Line(
                energy_term.get_corner(DL) + LEFT * 0.05,
                energy_term.get_corner(UR) + RIGHT * 0.05,
                color=RED,
                stroke_width=2
            )
            zero_label = MathTex("0", font_size=22, color=RED).next_to(energy_term, UP, buff=0.15)
            self.play(Create(slash), FadeIn(zero_label), run_time=tracker.duration * 0.4)
        self.wait(0.5)

        w_c = MathTex("W_C", font_size=24)
        w_c_eq_group = VGroup(w_c, equals.copy(), tr_top.copy(), oint_2.copy(), frac_group.copy()).arrange(RIGHT, buff=0.15)
        w_c_eq_group.move_to(RIGHT * 2.2 + UP * 1.5)

        with self.voiceover(text="This leaves us with the net work of the combined cycle, W C, equal to T R times the cyclic integral of delta Q over T.") as tracker:
            self.play(
                FadeOut(oint_1, eq1_lhs, energy_term, slash, zero_label),
                FadeIn(w_c),
                w_c.animate.move_to(w_c_eq_group[0]),
                equals.animate.move_to(w_c_eq_group[1]),
                tr_top.animate.move_to(w_c_eq_group[2]),
                oint_2.animate.move_to(w_c_eq_group[3]),
                frac_group.animate.move_to(w_c_eq_group[4]),
                run_time=tracker.duration
            )
        self.wait(0.5)

        # --- BLOCK 6: Inequality ---
        ineq_rhs = MathTex(r"\le 0", font_size=26, color=YELLOW)
        clausius_group = VGroup(oint_2.copy(), frac_group.copy(), ineq_rhs).arrange(RIGHT, buff=0.15)
        clausius_group.move_to(RIGHT * 2.2 + UP * 0.5)

        with self.voiceover(text="By the Kelvin-Planck statement of the second law, W C cannot be a positive quantity. Since T R is an absolute temperature and therefore positive, the cyclic integral of delta Q over T must be less than or equal to zero.") as tracker:
            self.play(
                FadeOut(tr_top, w_c, equals),
                oint_2.animate.move_to(clausius_group[0]),
                frac_group.animate.move_to(clausius_group[1]),
                FadeIn(ineq_rhs),
                run_time=tracker.duration * 0.7
            )
            final_box = SurroundingRectangle(VGroup(oint_2, frac_group, ineq_rhs), color=GREEN, buff=0.2)
            self.play(Create(final_box), run_time=tracker.duration * 0.3)
        
        self.wait(3)

        