from manim import *
from manim_voiceover import VoiceoverScene
from _010voice_helper import EdgeTTSService


class ReversibleHeatEngine(VoiceoverScene):
    def construct(self):
        self.set_speech_service(EdgeTTSService(voice="en-US-AndrewNeural"))

        # --- COLOR THEMES ---
        HOT_FILL = "#FF6B6B"    # Warm red
        HOT_STROKE = RED_D
        COLD_FILL = "#4ECDC4"   # Cool blue
        COLD_STROKE = BLUE_D
        ARROW_GREY = GRAY
        
        # ====================================================================
        # PART 1: DRAWING THE HEAT ENGINE & RESERVOIRS (Shifted left for landscape balance)
        # ====================================================================
        center_shift = LEFT * 2.0

        # 1. THE ENGINE (Center-Left)
        engine_circle = Circle(radius=1.1, color=WHITE, stroke_width=3, fill_opacity=0.1).move_to(center_shift)
        
        engine_text = Paragraph(
            "Reversible",
            "heat engine",
            "or",
            "refrigerator",
            font_size=18,
            alignment="center",
            font="Times New Roman",
            line_spacing=1.0
        ).move_to(engine_circle.get_center())
        
        # 2. HIGH-TEMPERATURE RESERVOIR (Top - Red Theme)
        th_shape = RoundedRectangle(
            corner_radius=0.35, width=4.0, height=0.9,
            fill_color=HOT_FILL, fill_opacity=0.6, stroke_color=HOT_STROKE, stroke_width=3
        )
        th_text = VGroup(
            Text("High-temperature reservoir", font_size=16, font="Times New Roman"),
            MathTex(r"at \ T_H", font_size=22)
        ).arrange(DOWN, buff=0.05).move_to(th_shape.get_center())
        
        th_group = VGroup(th_shape, th_text).next_to(engine_circle, UP, buff=0.8)

        # 3. LOW-TEMPERATURE RESERVOIR (Bottom - Blue Theme)
        tl_shape = RoundedRectangle(
            corner_radius=0.35, width=4.0, height=0.9,
            fill_color=COLD_FILL, fill_opacity=0.6, stroke_color=COLD_STROKE, stroke_width=3
        )
        tl_text = VGroup(
            Text("Low-temperature reservoir", font_size=16, font="Times New Roman"),
            MathTex(r"at \ T_L", font_size=22)
        ).arrange(DOWN, buff=0.05).move_to(tl_shape.get_center())
        
        tl_group = VGroup(tl_shape, tl_text).next_to(engine_circle, DOWN, buff=0.8)

        # 4. HEAT AND WORK ARROWS
        qh_solid = Arrow(th_shape.get_bottom() + RIGHT*0.25, engine_circle.get_top() + RIGHT*0.25, 
                         color=RED_B, buff=0.1, stroke_width=3.5, max_tip_length_to_length_ratio=0.2)
        qh_dashed = DashedLine(engine_circle.get_top() + LEFT*0.25, th_shape.get_bottom() + LEFT*0.25, 
                               color=RED_B, dash_length=0.1, stroke_width=2.5).add_tip(tip_length=0.12)
        qh_label = MathTex("Q_H", font_size=26).next_to(qh_solid, RIGHT, buff=0.3)

        ql_solid = Arrow(engine_circle.get_bottom() + RIGHT*0.25, tl_shape.get_top() + RIGHT*0.25, 
                         color=BLUE_B, buff=0.1, stroke_width=3.5, max_tip_length_to_length_ratio=0.2)
        ql_dashed = DashedLine(tl_shape.get_top() + LEFT*0.25, engine_circle.get_bottom() + LEFT*0.25, 
                               color=BLUE_B, dash_length=0.1, stroke_width=2.5).add_tip(tip_length=0.12)
        ql_label = MathTex("Q_L", font_size=26).next_to(ql_solid, RIGHT, buff=0.3)

        w_solid = Arrow(engine_circle.get_right() + UP*0.18, engine_circle.get_right() + RIGHT*1.4 + UP*0.18, 
                        color=ARROW_GREY, buff=0, stroke_width=3.5, max_tip_length_to_length_ratio=0.25)
        w_dashed = DashedLine(engine_circle.get_right() + RIGHT*1.4 + DOWN*0.18,engine_circle.get_right() + DOWN*0.18,  
                              color=ARROW_GREY, dash_length=0.1, stroke_width=2.5).add_tip(tip_length=0.12)
        w_label = MathTex("W_{net}", font_size=26).next_to(w_solid, UP, buff=0.08)

        # --- ANIMATE SCENE WITH SYNCED VOICEOVER ---
        with self.voiceover(text="Let us consider a reversible heat engine or refrigerator operating between two thermal reservoirs.") as tracker:
            self.play(
                DrawBorderThenFill(engine_circle), FadeIn(engine_text, shift=UP*0.2),
                FadeIn(th_group, shift=DOWN*0.3), FadeIn(tl_group, shift=UP*0.3),
                run_time=tracker.duration
            )

        with self.voiceover(text="Heat is transferred from the high-temperature reservoir, and rejected to the low-temperature reservoir, producing or consuming net work.") as tracker:
            self.play(
                GrowArrow(qh_solid), Create(qh_dashed), Write(qh_label),
                GrowArrow(ql_solid), Create(ql_dashed), Write(ql_label),
                GrowArrow(w_solid), Create(w_dashed), Write(w_label),
                run_time=tracker.duration
            )

        # ====================================================================
        # PART 2: THE EQUATION (Right side layout for landscape view)
        # ====================================================================
        equation = MathTex(
            r"\frac{Q_H}{Q_L} = \frac{T_H}{T_L}",
            font_size=46
        ).move_to([2.8, 0, 0])

        eq_box = SurroundingRectangle(equation, color=YELLOW, buff=0.2, stroke_width=2)

        with self.voiceover(text="Assuming you know that, for reversible cycles, the heat transfer ratio Q H over Q L can be replaced by the absolute temperature ratio T H over T L.") as tracker:
            self.play(
                Write(equation),
                run_time=tracker.duration
            )
        
        self.play(Create(eq_box))
        self.wait(2)
