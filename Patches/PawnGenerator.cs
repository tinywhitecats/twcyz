using HarmonyLib;
using RimWorld;
using System.Collections.Generic;
using System.Reflection;
using Verse;

namespace twcyz
{
    [HarmonyPatch]
    static class TWCYZ_PawnGenerator
    {
        static void Postfix(ref Pawn __result)
        {
            if (__result.story == null)
                return;
            foreach (BackstoryDef b in __result.story.AllBackstories)
            {
                if (b.HasModExtension<TWCYZAddHediff>())
                {
                    TWCYZAddHediff ext = b.GetModExtension<TWCYZAddHediff>();
                    foreach (BodyPartRecord bpr in __result.RaceProps.body.GetPartsWithDef(ext.bodypart)) {
                        __result.health.AddHediff(ext.hediff, bpr);
                    }
                }
            }
        }
        static IEnumerable<MethodBase> TargetMethods()
        {
            yield return AccessTools.Method(AccessTools.TypeByName("Verse.PawnGenerator"), "GenerateNewPawnInternal");
        }
    }
}