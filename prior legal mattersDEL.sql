-- prior legal matters
(
    AND (
        2 INTAKE_CLOSE_DATE >= 7 / 1 / 2022 3
        OR (CASE_STATUS = OPEN)
        OR (
            4
            AND CASE_STATUS = Closed 5
            AND CASE_CLOSE_DATE >= 7 / 1 / 2022
        )
    ) 6
    AND CASE_OWNER <> (
        Admin User,
        Bruce Mayor,
        Carmen Ramirez,
        Dimitri McDaniel,
        Jennifer Schlissel,
        Jihad Beauchman,
        Jillian Willis,
        Lauren Lowenstein,
        Lindsy Miles - Hare,
        Mateo Caballero,
        Phylisa Carter,
        Stacy Cloyd,
        Taylor Healy,
        Vytas Vergeer,
        Zahra Kahn,
        Zahra Khan
    ) 7
    AND INTAKE_DISPOSITION = BRIEF_SERVICE_OPEN,
    BRIEF_SERVICE_CLOSED..ETC 1 ---\
    ---
    (
        (
            1
            OR 2
            OR 3
            OR (
                4
                AND 5
            )
            AND (
                6
                AND 7
            )
        )
    )
    OR (
        8
        AND 9
        AND 10
    ) ------
) 1014 = 897 + 246