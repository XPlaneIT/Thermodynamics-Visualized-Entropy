from manim import *


class ReversibleHeatEngine(Scene):
    def construct(self):
        # --- COLOR THEMES ---
        HOT_FILL = "#FF6B6B"    # Warm red
        HOT_STROKE = RED_D
        COLD_FILL = "#4ECDC4"   # Cool blue
        COLD_STROKE = BLUE_D
        ARROW_GREY = GRAY
        
        # ====================================================================
        # VOICEOVER: "Assuming you know of this property of a reversible engine..."
        # ====================================================================
        
        # 1. THE ENGINE (Center)
        engine_circle = Circle(radius=1.2, color=WHITE, stroke_width=3, fill_opacity=0.1)
        
        engine_text = Paragraph(
            "Reversible",
            "heat engine",
            "or",
            "refrigerator",
            font_size=20,
            alignment="center",
            font="Times New Roman",
            line_spacing=1.0
        ).move_to(engine_circle.get_center())
        
        self.play(DrawBorderThenFill(engine_circle), FadeIn(engine_text, shift=UP*0.2))
        self.wait(0.5)

        # 2. HIGH-TEMPERATURE RESERVOIR (Top - Red Theme)
        th_shape = RoundedRectangle(
            corner_radius=0.4, width=4.5, height=1.0,
            fill_color=HOT_FILL, fill_opacity=0.6, stroke_color=HOT_STROKE, stroke_width=3
        )
        th_text = VGroup(
            Text("High-temperature reservoir", font_size=18, font="Times New Roman"),
            MathTex("at \ T_H", font_size=24)
        ).arrange(DOWN, buff=0.05).move_to(th_shape.get_center())
        
        th_group = VGroup(th_shape, th_text).next_to(engine_circle, UP, buff=1.0)

        # 3. LOW-TEMPERATURE RESERVOIR (Bottom - Blue Theme)
        tl_shape = RoundedRectangle(
            corner_radius=0.4, width=4.5, height=1.0,
            fill_color=COLD_FILL, fill_opacity=0.6, stroke_color=COLD_STROKE, stroke_width=3
        )
        tl_text = VGroup(
            Text("Low-temperature reservoir", font_size=18, font="Times New Roman"),
            MathTex("at \ T_L", font_size=24)
        ).arrange(DOWN, buff=0.05).move_to(tl_shape.get_center())
        
        tl_group = VGroup(tl_shape, tl_text).next_to(engine_circle, DOWN, buff=1.0)

        self.play(
            FadeIn(th_group, shift=DOWN*0.5),
            FadeIn(tl_group, shift=UP*0.5)
        )
        self.wait(0.5)

        # 4. HEAT AND WORK ARROWS
        # Q_H Arrows (Solid red down, Dashed red up)
        qh_solid = Arrow(th_shape.get_bottom() + LEFT*0.2, engine_circle.get_top() + LEFT*0.2, 
                         color=RED_B, buff=0.1, stroke_width=4)
        qh_dashed = DashedLine(th_shape.get_bottom() + RIGHT*0.2, engine_circle.get_top() + RIGHT*0.2, 
                               color=RED_B, stroke_width=3).add_tip()
        qh_label = MathTex("Q_H", font_size=28).next_to(qh_dashed, RIGHT, buff=0.2)

        # Q_L Arrows (Solid blue down, Dashed blue up)
        ql_solid = Arrow(engine_circle.get_bottom() + LEFT*0.2, tl_shape.get_top() + LEFT*0.2, 
                         color=BLUE_B, buff=0.1, stroke_width=4)
        ql_dashed = DashedLine(engine_circle.get_bottom() + RIGHT*0.2, tl_shape.get_top() + RIGHT*0.2, 
                               color=BLUE_B, stroke_width=3).add_tip()
        ql_label = MathTex("Q_L", font_size=28).next_to(ql_dashed, RIGHT, buff=0.2)

        # W_net Arrows (Neutral grey right and left)
        w_solid = Arrow(engine_circle.get_right() + UP*0.2, engine_circle.get_right() + RIGHT*1.8 + UP*0.2, 
                        color=ARROW_GREY, buff=0, stroke_width=4)
        w_dashed = DashedLine(engine_circle.get_right() + DOWN*0.2, engine_circle.get_right() + RIGHT*1.8 + DOWN*0.2, 
                              color=ARROW_GREY, stroke_width=3).add_tip()
        w_label = MathTex("W_{net}", font_size=28).next_to(w_solid, UP, buff=0.1)

        # Animate arrows
        self.play(GrowArrow(qh_solid), Create(qh_dashed), Write(qh_label))
        self.play(GrowArrow(ql_solid), Create(ql_dashed), Write(ql_label))
        self.play(GrowArrow(w_solid), Create(w_dashed), Write(w_label))
        self.wait(1)

        # ====================================================================
        # VOICEOVER: "For reversible cycles, the heat transfer ratio QH/QL 
        # can be equated with the absolute temperature ratio TH/TL."
        # ====================================================================
        
        # 5. THE RELATIONSHIP EQUATION (Right side)
        equation = MathTex(
            r"\frac{Q_H}{Q_L} = \frac{T_H}{T_L}",
            font_size=48
        ).next_to(w_solid, RIGHT, buff=1.2)

        self.play(Write(equation), run_time=1.5)
        self.wait(2)



class ClausiusInequalityDiagram(Scene):
    def construct(self):
        # ====================================================================
        # 1. SETTING UP COLORS AND STYLES
        # ====================================================================
        PINK_FILL = "#F9C6D9"
        PINK_STROKE = "#E872A0"
        
        # ====================================================================
        # 2. BUILDING THE DIAGRAM (Static Elements)
        # ====================================================================
        
        # --- Thermal Reservoir (Top) ---
        reservoir_shape = RoundedRectangle(
            corner_radius=0.3, width=4, height=0.5,
            fill_color=RED, fill_opacity=0.8, stroke_color=PINK_STROKE, stroke_width=1
        ).to_edge(UP, buff=0.5)
        
        reservoir_text = VGroup(
            Text("Thermal reservoir at ", font_size=20),
            MathTex("T_R", font_size=24)
        ).arrange(RIGHT, buff=0.1).move_to(reservoir_shape.get_center())
        
        reservoir = VGroup(reservoir_shape, reservoir_text)

        # --- Reversible Cyclic Device (Middle) ---
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

        # --- System (Bottom) ---
        system_rect = Rectangle(
            width=1.4, height=0.8, color=WHITE, stroke_width=2
        ).shift(DOWN * 1.4)
        
        system_text = Text("System", font_size=20).move_to(system_rect.get_center())
        temp_label = MathTex("T", font_size=24).next_to(system_rect, UP, buff=0.1).shift(LEFT*0.8)
        
        system = VGroup(system_rect, system_text, temp_label)

        # --- Combined System (Dashed Box) ---
        rect_shape = Rectangle(width=3, height=4.2, color=WHITE, stroke_width=2)
        dashed_box = DashedVMobject(rect_shape, num_dashes=50).shift(LEFT * 0.5)
        
        box_label = Text(
            "Combined system\n(system and cyclic device)", font_size=16, line_spacing=0.8
        ).next_to(dashed_box, DOWN * 0.5, buff=0.2)

        # --- Arrows ---
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

        self.play(FadeIn(diagram), run_time=2)
        self.wait(1)

        # ====================================================================
        # 3. THE POINTER ANIMATION
        # ====================================================================
        
        pointer = Arrow(ORIGIN, RIGHT, color=YELLOW, stroke_width=6, max_tip_length_to_length_ratio=0.3)
        
        pointer.next_to(reservoir, LEFT, buff=0.2)
        self.play(FadeIn(pointer), run_time=0.3)
        self.wait(0.8)
        
        self.play(pointer.animate.next_to(device_text, LEFT, buff=0.2), run_time=1)
        self.wait(0.8)
        
        self.play(pointer.animate.next_to(dq_r_label, RIGHT, buff=0.2).rotate(PI), run_time=0.8)
        self.wait(0.8)
        
        self.play(pointer.animate.next_to(temp_label, LEFT, buff=0.2).rotate(PI), run_time=0.8)
        self.wait(0.8)
        
        self.play(pointer.animate.next_to(dw_rev_label, UP, buff=0.2).rotate(-PI/2), run_time=0.8)
        self.wait(0.8)
        
        self.play(pointer.animate.next_to(dw_sys_label, UP, buff=0.2), run_time=1)
        self.wait(0.8)
        
        self.play(FadeOut(pointer))
        self.wait(0.5)

        # "Zoom zoom" - quick scale up and back down twice
        # We use rate_func=there_and_back to make it smoothly return to normal size
        self.play(
            dashed_box.animate.scale(1.1), 
            run_time=0.3, 
            rate_func=there_and_back
        )
        self.play(
            dashed_box.animate.scale(1.1), 
            run_time=0.3, 
            rate_func=there_and_back
        )

        # ====================================================================
        # 4. PUSH DIAGRAM LEFT AND PREPARE TERMS
        # ====================================================================
        
        self.play(diagram.animate.to_edge(LEFT, buff=0.5))

        # Create copies at the exact starting positions of the originals
        dQ_R = dq_r_label.copy()
        dW_rev = dw_rev_label.copy()
        dW_sys = dw_sys_label.copy()

        # --- BLOCK 1: Build dW_C = dW_rev + dW_sys -> dQ_R - dE_C ---
        eq1_lhs = MathTex(r"\delta W_C", font_size=24)
        equals = MathTex("=", font_size=24)
        plus = MathTex("+", font_size=24)
        target_rev = dW_rev.copy()
        target_sys = dW_sys.copy()

        row1_targets = VGroup(eq1_lhs, equals, target_rev, plus, target_sys).arrange(RIGHT, buff=0.15)
        row1_targets.move_to(RIGHT * 2.5 + UP * 2.5)
        
        self.play(
                    dW_rev.animate.move_to(target_rev),
                    dW_sys.animate.move_to(target_sys),
                    run_time=1.5
                )
        self.play(FadeIn(eq1_lhs, equals, plus))
        self.wait(1)
        
        self.play(FadeOut(dW_rev, plus, dW_sys))
        self.wait(0.5)

        eq2_rhs = MathTex(r"- \delta E_C", font_size=24)
        target_dqr = dQ_R.copy()
        
        row2_rhs = VGroup(target_dqr, eq2_rhs).arrange(RIGHT, buff=0.15)
        row2_rhs.next_to(equals, RIGHT, buff=0.15)
        
        self.play(dQ_R.animate.move_to(target_dqr), run_time=1.5)
        self.play(FadeIn(eq2_rhs))
        self.wait(1.5)

        # --- BLOCK 2: Fly dQ_R, T_R, dQ, and T to form dQ_R / T_R = dQ / T ---
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

        self.play(
            dQ_R_2.animate.move_to(target_dqr_2),
            T_R.animate.move_to(target_tr),
            dQ.animate.move_to(target_dq),
            T.animate.move_to(target_t),
            run_time=1.8
        )
        self.play(Create(bar_left), Create(bar_right), FadeIn(equals_2))
        self.wait(1.5)

    # --- BLOCK 3: Solve for dQ_R -> dQ_R = T_R (dQ / T) ---
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

        self.play(
            FadeOut(bar_left),
            dQ_R_2.animate.move_to(solved_dqr),
            equals_2.animate.move_to(solved_eq),
            T_R.animate.move_to(solved_tr),
            dQ.animate.move_to(solved_dq),
            bar_right.animate.move_to(solved_bar),
            T.animate.move_to(solved_t),
            FadeIn(left_paren, right_paren),
            run_time=1.8
        )
        self.wait(1.5)

# --- BLOCK 4: Substitute T_R (dQ / T) into dW_C = dQ_R - dE_C ---
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
        self.play(Create(sub_arrow))
        self.wait(0.8)

        self.play(
            FadeOut(dQ_R, sub_arrow),
            eq2_rhs.animate.move_to(sub_dec_target),
            rhs_copy.animate.move_to(sub_rhs_target),
            run_time=1.8
        )
        self.wait(1.5)

        # Fade out the helper equation on the bottom row to focus on the cycle
        self.play(FadeOut(dQ_R_2, equals_2, rhs_expr))
        self.wait(0.5)

# --- BLOCK 5: Apply Cyclic Integral -> W_C = T_R \oint (dQ / T) ---
        # Unpack rhs_copy pieces: [0]=T_R, [1]=(, [2]=dQ, [3]=bar, [4]=T, [5]=)
        tr_top = rhs_copy[0]
        frac_group = VGroup(rhs_copy[1], rhs_copy[2], rhs_copy[3], rhs_copy[4], rhs_copy[5])

        # Create cyclic integral symbols and new W_C label
        oint_1 = MathTex(r"\oint", font_size=28)
        oint_2 = MathTex(r"\oint", font_size=28)
        oint_3 = MathTex(r"\oint", font_size=28)
        minus_sign = MathTex("-", font_size=24)
        dec_term = MathTex(r"\delta E_C", font_size=24)

        # Target layout for integrated equation: \oint dW_C = T_R \oint (dQ/T) - \oint dE_C
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
            run_time=1.8
        )
        self.wait(1)

        # Show cyclic integral of energy is zero (property of a cycle)
        energy_term = VGroup(minus_sign, oint_3, dec_term)
        slash = Line(
            energy_term.get_corner(DL) + LEFT * 0.05,
            energy_term.get_corner(UR) + RIGHT * 0.05,
            color=RED,
            stroke_width=2
        )
        zero_label = MathTex("0", font_size=22, color=RED).next_to(energy_term, UP, buff=0.15)

        self.play(Create(slash), FadeIn(zero_label))
        self.wait(1.2)

        # Simplify \oint \delta W_C -> W_C and remove the zero energy term
        w_c = MathTex("W_C", font_size=24)
        w_c_eq_group = VGroup(w_c, equals.copy(), tr_top.copy(), oint_2.copy(), frac_group.copy()).arrange(RIGHT, buff=0.15)
        w_c_eq_group.move_to(RIGHT * 2.2 + UP * 1.5)

        self.play(
            FadeOut(oint_1, eq1_lhs, energy_term, slash, zero_label),
            FadeIn(w_c),
            w_c.animate.move_to(w_c_eq_group[0]),
            equals.animate.move_to(w_c_eq_group[1]),
            tr_top.animate.move_to(w_c_eq_group[2]),
            oint_2.animate.move_to(w_c_eq_group[3]),
            frac_group.animate.move_to(w_c_eq_group[4]),
            run_time=1.5
        )
        self.wait(1.5)

        # --- BLOCK 6: Fade out T_R and conclude Clausius Inequality \oint (dQ / T) <= 0 ---
        # By Kelvin-Planck, W_C <= 0 and T_R > 0, so T_R fades out and we conclude \oint (dQ/T) <= 0
        ineq_rhs = MathTex(r"\le 0", font_size=26, color=YELLOW)
        clausius_group = VGroup(oint_2.copy(), frac_group.copy(), ineq_rhs).arrange(RIGHT, buff=0.15)
        clausius_group.move_to(RIGHT * 2.2 + UP * 0.5)

        self.play(
            FadeOut(tr_top, w_c, equals),
            oint_2.animate.move_to(clausius_group[0]),
            frac_group.animate.move_to(clausius_group[1]),
            FadeIn(ineq_rhs),
            run_time=1.8
        )
        self.wait(0.8)

        # Highlight the final Clausius Inequality
        final_box = SurroundingRectangle(VGroup(oint_2, frac_group, ineq_rhs), color=GREEN, buff=0.2)
        self.play(Create(final_box))
        self.wait(3)







class EntropyDefinition(Scene):
    def construct(self):
        # ====================================================================
        # FRAME & MARGIN LAYOUT CONSTANTS
        # Safe usable zone with ~0.6 margin: x in [-6.5, 6.5], y in [-3.4, 3.4]
        # ====================================================================
        LEFT_COL_X = -3.4
        RIGHT_COL_X = 3.3

        # ====================================================================
        # PART 1: THE MATHEMATICAL PROOF (P-V Diagram)
        # ====================================================================
        
        # 1. Setup the P-V Diagram (Left Column, safely within margins)
        axes_pv = Axes(
            x_range=[0, 10, 2], y_range=[0, 10, 2],
            x_length=4.5, y_length=4.5,
            axis_config={"include_tip": True, "include_numbers": False}
        ).move_to([LEFT_COL_X, -0.2, 0])
        
        v_label = axes_pv.get_x_axis_label("V", edge=RIGHT, direction=DOWN, buff=0.15)
        p_label = axes_pv.get_y_axis_label("P", edge=UP, direction=LEFT, buff=0.15)
        
        # Define State 1 and State 2
        state_1_pv = axes_pv.c2p(2, 2)
        state_2_pv = axes_pv.c2p(8, 8)
        
        dot_1 = Dot(state_1_pv, color=WHITE)
        dot_2 = Dot(state_2_pv, color=WHITE)
        label_1 = MathTex("1", font_size=24).next_to(dot_1, DOWN + LEFT, buff=0.1)
        label_2 = MathTex("2", font_size=24).next_to(dot_2, UP + RIGHT, buff=0.1)
        
        # Draw the Two Paths
        path_A = ArcBetweenPoints(state_1_pv, state_2_pv, angle=-PI/3, color=BLUE)
        path_A_label = Text("Path A", font_size=18, color=BLUE).next_to(path_A, DOWN, buff=0.2)
        
        path_B = ArcBetweenPoints(state_1_pv, state_2_pv, angle=PI/3, color=RED)
        path_B_label = Text("Path B", font_size=18, color=RED).next_to(path_B, UP, buff=0.2)

        self.play(Create(axes_pv), Write(v_label), Write(p_label))
        self.play(FadeIn(dot_1, label_1), FadeIn(dot_2, label_2))
        self.play(Create(path_A), Write(path_A_label))
        self.play(Create(path_B), Write(path_B_label))
        self.wait(0.8)

        # 2. The Math Derivation (Right Column, Flying Terms)
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
        
        flip_eq = MathTex(
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{A}", r"-",
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{B}", r"=", r"0",
            font_size=25
        ).move_to(expand_eq)
        
        # Term (\int_1^2 \delta Q / T)_B flies across the '=' sign to the right side!
        final_eq = MathTex(
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{A}", r"=",
            r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{B}",
            font_size=26
        ).move_to(flip_eq)
        
        conclusion_text = Text(
            "The integral is path-independent!\nThis defines a property:",
            font_size=18, line_spacing=1.2, color=YELLOW
        ).next_to(final_eq, DOWN, buff=0.7)
        
        entropy_eq = MathTex(
            r"\Delta S", r"=", r"S_2 - S_1", r"=", r"\int_{1}^{2}", r"\left(\frac{\delta Q}{T}\right)_{rev}",
            font_size=26, color=GREEN
        ).next_to(conclusion_text, DOWN, buff=0.45)

        entropy_box = SurroundingRectangle(entropy_eq, color=GREEN, buff=0.12)

        self.play(Write(intro_text), Write(cyclic_eq))
        self.wait(0.6)
        self.play(TransformMatchingTex(cyclic_eq, expand_eq, path_arc=PI/4), run_time=1.2)
        self.wait(0.6)
        self.play(TransformMatchingTex(expand_eq, flip_eq, path_arc=PI/4), run_time=1.2)
        self.wait(0.6)
        self.play(TransformMatchingTex(flip_eq, final_eq, path_arc=PI/2), run_time=1.4)
        self.wait(0.6)

        self.play(FadeIn(conclusion_text, shift=UP * 0.2))
        self.play(
            TransformMatchingTex(final_eq.copy(), entropy_eq, path_arc=PI/4),
            run_time=1.3
        )
        self.play(Create(entropy_box))
        self.wait(1.8)

        # ====================================================================
        # PART 2: REPLACING WITH THE T-S DIAGRAM (Centered, Safe Margins)
        # ====================================================================
        part1_group = VGroup(
            axes_pv, v_label, p_label, dot_1, dot_2, label_1, label_2,
            path_A, path_A_label, path_B, path_B_label,
            intro_text, final_eq, conclusion_text, entropy_eq,
            entropy_box
        )
        self.play(FadeOut(part1_group), run_time=1.2)
        self.wait(0.4)

        # 1. Setup the T-S Diagram (Sized so top equation & bottom caption have room)
        axes_ts = Axes(
            x_range=[0, 1, 0.1], y_range=[0, 5, 1],
            x_length=6.4, y_length=4.2,
            axis_config={"include_tip": True, "include_numbers": False, "stroke_width": 2},
            tips=True
        ).move_to([-0.2, -0.15, 0])
        
        t_axis_label = MathTex("T", font_size=28).next_to(axes_ts.y_axis.get_end(), UP, buff=0.1)
        s_axis_label = MathTex(r"S, \ \text{kJ/K}", font_size=26).next_to(axes_ts.x_axis.get_end(), RIGHT, buff=0.15)

        # 2. Define State 1 and 2 on the T-S Diagram
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

        # 3. The Two Paths (Scaled control points to stay compact)
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

        # Arrows sampled directly on the curves
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

        # 4. Labels and Pointers (Placed cleanly inside the plot region)
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

        # 5. Top Equation & Bottom Caption (Inside safe top/bottom margins)
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
        self.play(Create(axes_ts), Write(t_axis_label), Write(s_axis_label))
        self.play(FadeIn(dot1_ts, label1_ts, dot2_ts, label2_ts))
        self.play(Create(proj_1), Create(proj_2), Write(s_val_1), Write(s_val_2))
        self.wait(0.4)
        
        # Draw the Reversible (Solid) Path
        self.play(Create(path_rev), FadeIn(arrow_rev), run_time=1.4)
        self.play(Write(text_rev), Create(pointer_rev))
        self.wait(0.4)
        
        # Draw the Irreversible (Dashed) Path
        self.play(Create(path_irrev), FadeIn(arrow_irrev), run_time=1.4)
        self.play(Write(text_irrev), Create(pointer_irrev))
        self.wait(0.8)
        
        # Show the Math and Caption
        self.play(Write(delta_s_eq))
        self.play(FadeIn(caption, shift=UP * 0.2))
        self.wait(2)








class EntropyGeneration(Scene):
    def construct(self):
        # ====================================================================
        # FRAME & MARGIN LAYOUT CONSTANTS
        # Manim default frame: 14.22 wide (-7.11 to 7.11) x 8.0 high (-4.0 to 4.0)
        # Safe usable zone with 0.6 margin: x in [-6.5, 6.5], y in [-3.4, 3.4]
        # ====================================================================
        LEFT_COL_X = -3.4
        RIGHT_COL_X = 3.3

        # ====================================================================
        # 1. SETUP THE T-S DIAGRAM (Left Column, well within margins)
        # ====================================================================
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 5, 1],
            x_length=4.5, y_length=4.5,
            axis_config={"include_tip": True, "include_numbers": False}
        ).move_to([LEFT_COL_X, -0.3, 0])
        
        t_label = axes.get_y_axis_label("T", edge=UP, direction=LEFT, buff=0.15)
        s_label = axes.get_x_axis_label("S", edge=RIGHT, direction=DOWN, buff=0.15)

        # Define State 1 (bottom left) and State 2 (top right)
        state_1 = axes.c2p(1.0, 1.3)
        state_2 = axes.c2p(4.0, 4.2)
        
        dot1 = Dot(state_1, color=WHITE)
        dot2 = Dot(state_2, color=WHITE)
        label1 = MathTex("1", font_size=24).next_to(dot1, DOWN + LEFT, buff=0.1)
        label2 = MathTex("2", font_size=24).next_to(dot2, UP + RIGHT, buff=0.1)

        # Path 1-2 (Arbitrary, Dashed) - Curves upward
        path_12_curve = CubicBezier(
            state_1,
            state_1 + RIGHT * 1.2 + UP * 2.0,
            state_2 + LEFT * 1.6 + UP * 0.4,
            state_2,
            color=ORANGE, stroke_width=3.5
        )
        path_12 = DashedVMobject(path_12_curve, num_dashes=26)
        
        # Path 2-1 (Internally reversible, Solid) - Curves downward
        path_21 = CubicBezier(
            state_2,
            state_2 + LEFT * 1.2 + DOWN * 2.0,
            state_1 + RIGHT * 1.6 + DOWN * 0.4,
            state_1,
            color=ORANGE, stroke_width=3.5
        )

        # Arrows placed directly on the curves
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

        # Compact labels & pointers positioned safely inside left margin
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

        # Animate the T-S Diagram
        self.play(Create(axes), Write(t_label), Write(s_label))
        self.play(FadeIn(dot1, label1, dot2, label2))
        self.play(Create(path_12), FadeIn(arrow_12), Write(text_12), Create(ptr_12))
        self.play(Create(path_21), FadeIn(arrow_21), Write(text_21), Create(ptr_21))
        self.wait(0.8)

        # ====================================================================
        # 2. THE MATHEMATICAL DERIVATION (Right Column, Flying Terms)
        # ====================================================================
        
        # Step 1: Clausius Inequality
        eq1 = MathTex(
            r"\oint", r"\frac{\delta Q}{T}", r"\leq", r"0",
            font_size=34
        ).move_to([RIGHT_COL_X, 2.7, 0])
        self.play(Write(eq1))
        self.wait(0.8)

        # Step 2: Split integral into two paths (fly \delta Q / T and \leq 0 down from eq1)
        eq2 = MathTex(
            r"\int_{1}^{2}", r"\frac{\delta Q}{T}", r"+", r"\int_{2}^{1} \left(\frac{\delta Q}{T}\right)_{rev}", r"\leq", r"0",
            font_size=28
        ).move_to([RIGHT_COL_X, 1.4, 0])
        
        self.play(
            TransformMatchingTex(eq1.copy(), eq2, path_arc=PI/4),
            run_time=1.3
        )
        self.wait(0.8)

        # Step 3: Highlight reversible integral & replace with (S_1 - S_2)
        highlight_rev = SurroundingRectangle(eq2[3], color=YELLOW, buff=0.08)
        self.play(Create(highlight_rev))
        self.wait(0.4)

        eq3 = MathTex(
            r"\int_{1}^{2}", r"\frac{\delta Q}{T}", r"+", r"(", r"S_1", r"-", r"S_2", r")", r"\leq", r"0",
            font_size=29
        ).move_to(eq2)

        self.play(
            FadeOut(highlight_rev),
            TransformMatchingTex(eq2, eq3, path_arc=PI/4),
            run_time=1.2
        )
        self.wait(0.8)

        # Step 4: Rearrange terms — S_2 and S_1 fly to the left side!
        eq4 = MathTex(
            r"S_2", r"-", r"S_1", r"\geq", r"\int_{1}^{2}", r"\frac{\delta Q}{T}",
            font_size=32
        ).move_to([RIGHT_COL_X, 1.3, 0])

        self.play(
            TransformMatchingTex(
                eq3, eq4,
                path_arc=PI/2,
                key_map={r"\leq": r"\geq"}
            ),
            run_time=1.5
        )
        self.wait(0.8)

        # Step 5: Differential form below eq4
        eq5 = MathTex(
            r"dS", r"\geq", r"\frac{\delta Q}{T}",
            font_size=32, color=YELLOW
        ).move_to([RIGHT_COL_X, 0.0, 0])
        
        self.play(
            TransformMatchingTex(eq4.copy(), eq5, path_arc=PI/4),
            run_time=1.2
        )
        self.wait(0.8)

        # ====================================================================
        # 3. INTRODUCING ENTROPY GENERATION (S_gen)
        # ====================================================================
        # Transform eq4 directly into eq6 so \int_1^2 \delta Q / T slides right
        # to make room for S_gen!
        eq6 = MathTex(
            r"\Delta S", r"=", r"\int_{1}^{2}", r"\frac{\delta Q}{T}", r"+", r"S_{gen}",
            font_size=32
        ).move_to(eq4)

        self.play(
            TransformMatchingTex(
                eq4, eq6,
                path_arc=PI/3,
                key_map={r"\geq": r"="}
            ),
            run_time=1.4
        )

        eq6_box = SurroundingRectangle(eq6, color=GREEN, buff=0.12)
        sgen_cond = MathTex(r"S_{gen} \geq 0", font_size=28, color=RED).next_to(eq6_box, DOWN, buff=0.25)

        # Shift eq5 slightly down so nothing crowds sgen_cond
        self.play(
            eq5.animate.move_to([RIGHT_COL_X, -1.5, 0]),
            Create(eq6_box),
            Write(sgen_cond),
            run_time=1.0
        )
        self.wait(1.8)

        # ====================================================================
        # 4. THE INCREASE OF ENTROPY PRINCIPLE
        # ====================================================================
        self.play(
            FadeOut(eq1, eq5, eq6, sgen_cond, eq6_box)
        )
        self.wait(0.4)

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

        self.play(Write(isolated_text))
        self.play(Write(isolated_eq), Create(isolated_box))
        self.play(FadeIn(principle_text, shift=UP * 0.2))
        self.wait(3)





class IncreaseOfEntropyPrinciple(Scene):
    def construct(self):
        # ====================================================================
        # FRAME & MARGIN LAYOUT CONSTANTS
        # Safe usable zone: x in [-6.5, 6.5], y in [-3.4, 3.4]
        # ====================================================================
        LEFT_COL_X = -3.4
        RIGHT_COL_X = 3.3

        # ====================================================================
        # PART 1: EXTENSIVE PROPERTY & SUBSYSTEMS (Fig. 7-6)
        # ====================================================================
        title_1 = Text("The Increase of Entropy Principle", font_size=26, color=YELLOW).to_edge(UP, buff=0.4)
        self.play(Write(title_1))

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

        self.play(Create(iso_outer), Write(iso_label))
        self.play(
            FadeIn(sub1, sub1_txt),
            FadeIn(sub2, sub2_txt),
            FadeIn(sub3, sub3_txt),
            Write(dots_sub),
            FadeIn(subN, subN_txt),
            run_time=1.3
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

        self.play(Write(ext_text))
        self.play(Write(sum_eq_1))
        self.wait(0.8)
        self.play(TransformMatchingTex(sum_eq_1, sum_eq_expanded, path_arc=PI/4), run_time=1.2)
        self.wait(1.0)

        # ====================================================================
        # PART 2: SYSTEM + SURROUNDINGS = ISOLATED SYSTEM (Fig. 7-7)
        # ====================================================================
        self.play(FadeOut(fig76_group), FadeOut(ext_text))

        # Build Piston-Cylinder System inside Isolated Boundary
        # Outer irregular isolated boundary (using RoundedRectangle/Ellipse)
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

        # Cylinder walls (U-shape with left inlet port)
        cyl_left_top = Line(
            [LEFT_COL_X - 0.95, 0.75, 0],
            [LEFT_COL_X - 0.95, -0.95, 0],
            color=WHITE, stroke_width=3
        )
        cyl_inlet_top = Line(
            [LEFT_COL_X - 0.95, -0.95, 0],
            [LEFT_COL_X - 1.25, -0.95, 0],
            color=WHITE, stroke_width=3
        )
        cyl_inlet_bot = Line(
            [LEFT_COL_X - 1.25, -1.15, 0],
            [LEFT_COL_X - 0.95, -1.15, 0],
            color=WHITE, stroke_width=3
        )
        cyl_bottom_right = VMobject(color=WHITE, stroke_width=3).set_points_as_corners([
            [LEFT_COL_X - 0.95, -1.15, 0],
            [LEFT_COL_X - 0.95, -1.35, 0],
            [LEFT_COL_X + 0.95, -1.35, 0],
            [LEFT_COL_X + 0.95, 0.75, 0]
        ])

        piston = Rectangle(
            width=1.86, height=0.25,
            color=GRAY_A, fill_color=GRAY, fill_opacity=0.9, stroke_width=1.5
        ).move_to([LEFT_COL_X, 0.25, 0])

        sys_box = DashedVMobject(
            Rectangle(width=1.72, height=1.35, color= ORANGE, stroke_width=2.5).move_to([LEFT_COL_X, -0.6, 0]),
            num_dashes=26
        )
        sys_lbl = Text("System", font_size=16).move_to(sys_box.get_center() + UP * 0.25)
        surr_lbl = Text("Surroundings", font_size=16, color=GRAY_A).move_to([LEFT_COL_X, -1.85, 0])

        # Internal transfer arrows (m, Q, W)
        m_arrow_in = CurvedArrow([LEFT_COL_X - 1.65, -0.85, 0], [LEFT_COL_X - 1.05, -1.02, 0], angle=0.3, tip_length=0.12, stroke_width=1.5)
        m_arrow_out = CurvedArrow([LEFT_COL_X - 1.05, -1.10, 0], [LEFT_COL_X - 1.65, -1.00, 0], angle=-0.3, tip_length=0.12, stroke_width=1.5)
        m_lbl = MathTex("m", font_size=20).next_to(m_arrow_in, UP, buff=0.05)

        qw_arrow_out = CurvedArrow([LEFT_COL_X + 0.65, -0.85, 0], [LEFT_COL_X + 1.45, -0.95, 0], angle=-0.2, tip_length=0.12, stroke_width=1.5)
        qw_arrow_in = CurvedArrow([LEFT_COL_X + 1.45, -1.12, 0], [LEFT_COL_X + 0.65, -1.02, 0], angle=0.2, tip_length=0.12, stroke_width=1.5)
        qw_lbl = MathTex("Q, W", font_size=20).next_to(qw_arrow_out, UP, buff=0.05)

        piston_fig = VGroup(
            boundary_outer, iso_bnd_lbl, iso_bnd_ptr, no_transfer_lbl, no_transfer_arr,
            cyl_left_top, cyl_inlet_top, cyl_inlet_bot, cyl_bottom_right,
            piston, sys_box, sys_lbl, surr_lbl,
            m_arrow_in, m_arrow_out, m_lbl, qw_arrow_out, qw_arrow_in, qw_lbl
        )

        self.play(Create(boundary_outer), Write(iso_bnd_lbl), Create(iso_bnd_ptr))
        self.play(Write(no_transfer_lbl), Create(no_transfer_arr))
        self.play(
            Create(cyl_left_top), Create(cyl_inlet_top), Create(cyl_inlet_bot), Create(cyl_bottom_right),
            FadeIn(piston), Create(sys_box), Write(sys_lbl), Write(surr_lbl)
        )
        self.play(
            Create(m_arrow_in), Create(m_arrow_out), Write(m_lbl),
            Create(qw_arrow_out), Create(qw_arrow_in), Write(qw_lbl)
        )

        # Right Column: Eq (7-11) Derivation with Flying Terms
        sys_surr_txt = Text(
            "System + Surroundings = Isolated System\n(No entropy transfer across outer boundary):",
            font_size=16, line_spacing=1.2
        ).move_to([RIGHT_COL_X, 2.25, 0])

        eq_711_step1 = MathTex(
            r"\Delta S_{\text{total}}", r"=", r"\Delta S_{\text{sys}}", r"+", r"\Delta S_{\text{surr}}", r"\geq", r"0",
            font_size=24
        ).move_to(sum_eq_expanded)

        self.play(Write(sys_surr_txt))
        self.play(
            TransformMatchingTex(sum_eq_expanded, eq_711_step1, path_arc=PI/3),
            run_time=1.4
        )
        self.wait(0.7)

        # Fly S_gen = in front of \Delta S_total!
        eq_711_final = MathTex(
            r"S_{\text{gen}}", r"=", r"\Delta S_{\text{total}}", r"=", r"\Delta S_{\text{sys}}", r"+", r"\Delta S_{\text{surr}}", r"\geq", r"0",
            font_size=22, color=GREEN
        ).move_to(eq_711_step1)

        self.play(
            TransformMatchingTex(eq_711_step1, eq_711_final, path_arc=PI/4),
            run_time=1.3
        )
        eq_711_box = SurroundingRectangle(eq_711_final, color=GREEN, buff=0.1)
        self.play(Create(eq_711_box))
        self.wait(1.0)

        # ====================================================================
        # PART 3: NEGATIVE SYSTEM ENTROPY CHANGE EXAMPLE (Fig. 7-8)
        # ====================================================================
        # Clean up internal arrows and labels from Fig. 7-7 to transition smoothly into Fig. 7-8
        fig77_only = VGroup(
            iso_bnd_lbl, iso_bnd_ptr, no_transfer_lbl, no_transfer_arr,
            m_arrow_in, m_arrow_out, m_lbl, qw_arrow_out, qw_arrow_in, qw_lbl,
            sys_lbl, surr_lbl
        )
        self.play(FadeOut(fig77_only), FadeOut(sys_surr_txt))

        # Add Fig. 7-8 labels & heat rejection arrow Q
        surr_top_78 = Text("Surroundings", font_size=16, color=GRAY_A).move_to([LEFT_COL_X, 1.45, 0])
        ds_sys_78 = MathTex(r"\Delta S_{\text{sys}} = -2\text{ kJ/K}", font_size=20, color=RED).move_to([LEFT_COL_X, -0.35, 0])
        sys_caps_78 = Text("SYSTEM", font_size=15).move_to([LEFT_COL_X, -0.8, 0])
        ds_surr_78 = MathTex(r"\Delta S_{\text{surr}} = 3\text{ kJ/K}", font_size=20, color=ORANGE).move_to([LEFT_COL_X, -1.8, 0])

        q_out_arrow = Arrow(
            [LEFT_COL_X + 0.55, -0.95, 0],
            [LEFT_COL_X + 1.55, -0.95, 0],
            color=ORANGE, stroke_width=5, max_tip_length_to_length_ratio=0.35
        )
        q_out_lbl = MathTex("Q", font_size=22, color=ORANGE).next_to(q_out_arrow, RIGHT, buff=0.1)

        self.play(
            Write(surr_top_78), Write(ds_sys_78), Write(sys_caps_78), Write(ds_surr_78),
            GrowArrow(q_out_arrow), Write(q_out_lbl)
        )

        # Right Column: Numerical substitution & 3-case criterion
        neg_note = Text(
            "A system's entropy can decrease (heat rejection),\nbut entropy generation CANNOT be negative:",
            font_size=16, line_spacing=1.2, color=YELLOW
        ).move_to([RIGHT_COL_X, 2.25, 0])

        num_eq = MathTex(
            r"S_{\text{gen}}", r"=", r"-2", r"+", r"3", r"=", r"+1\text{ kJ/K} > 0",
            font_size=24, color=WHITE
        ).next_to(eq_711_box, DOWN, buff=0.35)

        self.play(Write(neg_note))
        self.play(
            TransformMatchingTex(eq_711_final.copy(), num_eq, path_arc=PI/4),
            run_time=1.3
        )
        self.wait(1.0)

        # Show the 3 Criteria for S_gen
        criteria_box_title = Text("Increase of Entropy Principle:", font_size=17, color=YELLOW).next_to(num_eq, DOWN, buff=0.45)
        crit_irrev = MathTex(r"S_{\text{gen}} > 0 \quad \Rightarrow \quad \text{Irreversible process}", font_size=21, color=GREEN)
        crit_rev = MathTex(r"S_{\text{gen}} = 0 \quad \Rightarrow \quad \text{Reversible process}", font_size=21, color=BLUE_B)
        crit_imp = MathTex(r"S_{\text{gen}} < 0 \quad \Rightarrow \quad \text{Impossible process}", font_size=21, color=RED)

        criteria_group = VGroup(crit_irrev, crit_rev, crit_imp).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(
            criteria_box_title, DOWN, buff=0.25
        )

        self.play(Write(criteria_box_title))
        self.play(FadeIn(criteria_group, shift=UP * 0.15, lag_ratio=0.25), run_time=1.5)
        self.wait(2.2)

        # ====================================================================
        # PART 4: KEY REMARKS ABOUT ENTROPY (Centered Summary)
        # ====================================================================
        everything_part3 = VGroup(
            boundary_outer, cyl_left_top, cyl_inlet_top, cyl_inlet_bot, cyl_bottom_right,
            piston, sys_box, surr_top_78, ds_sys_78, sys_caps_78, ds_surr_78,
            q_out_arrow, q_out_lbl,
            neg_note, eq_711_final, eq_711_box, num_eq, criteria_box_title, criteria_group
        )
        self.play(FadeOut(everything_part3), run_time=1.0)

        remarks_header = Text("Key Conclusions About Entropy", font_size=24, color=GREEN).next_to(title_1, DOWN, buff=0.45)

        r1 = VGroup(
            Text("1. Direction of Processes:", font_size=19, color=YELLOW),
            Text(
                "Processes occur in one direction only (S_gen ≥ 0). Violations are impossible,\noften halting chemical reactions before full completion.",
                font_size=16, line_spacing=1.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        r2 = VGroup(
            Text("2. Nonconserved Property:", font_size=19, color=YELLOW),
            Text(
                "There is no conservation of entropy principle. Entropy is conserved only in\nidealized reversible processes and increases during all actual processes.",
                font_size=16, line_spacing=1.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        r3 = VGroup(
            Text("3. Measure of Irreversibility & Equilibrium:", font_size=19, color=YELLOW),
            Text(
                "Entropy generation quantifies irreversibilities that degrade engineering\ndevices. Isolated systems evolve until entropy reaches a maximum (equilibrium).",
                font_size=16, line_spacing=1.15
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        remarks_list = VGroup(r1, r2, r3).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(
            remarks_header, DOWN, buff=0.4
        )

        self.play(Write(remarks_header))
        self.play(FadeIn(r1, shift=RIGHT * 0.2))
        self.wait(0.8)
        self.play(FadeIn(r2, shift=RIGHT * 0.2))
        self.wait(0.8)
        self.play(FadeIn(r3, shift=RIGHT * 0.2))
        self.wait(3.0)
       